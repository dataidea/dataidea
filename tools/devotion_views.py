# OpenAi and LangChain
import os
import assemblyai as aai
from .models import Devotion
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from forms import DevotionForm, AudioUploadForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:signin')
def generateDevotion(request):
    form = DevotionForm()
    os.environ["OPENAI_API_KEY"] = "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"
    aai.settings.api_key = f"3282ce6eca0a47519f6f69dbbaa38da6"
    if request.method == 'POST':
        devotion_form = DevotionForm(request.POST)
        
        if devotion_form.is_valid():
            verse = devotion_form.cleaned_data['verse']
            audio_form = AudioUploadForm(request.POST, request.FILES)
            
            llm = OpenAI(temperature=0, model='gpt-3.5-turbo')

            devotion_prompt = '''
            I would like you to write me a "devotion" based on {scripture}, I have two examples of "devotion" that I want you to learn from. The first one is as below

            #IndisputableGeneration
            Tuesday 26th September 2023

            YOUR DAILY PRAYER IGNITE 
            BY Ap. Samuel Muyita

            John 12:3 Then took Mary a pound of ointment of spikenard, very costly, and anointed the feet of Jesus, and wiped his feet with her hair: and the house was filled with the odour of the ointment.

            SPENDING ON JESUS 

            It’s in the ways of God that He only trusts you with what you can give Him back. Anything you aren’t ready to spend on Him, you aren’t ready to receive!

            The scriptures are clear, “For where your treasure is, there will your heart be also” Matthew 6:21. Whenever our hearts are fully given to Him, our treasures too will be!

            In our theme scripture, we see Mary, taking something very costly and spending it on Jesus! Judas called it wasting, but Jesus saw it as love! She added on that and laid her crown of glory (hair) at the feet of Jesus to wipe His feet!

            Whatever we spend on behalf of God is not wasted, but it’s a statement to heaven that we understand where our treasure is, and there our hearts also will be!

            Your heart will be tested, God will try you with a little of what you think you are ready for, and oftentimes, many eyes are blinded by the hand of God that they miss His heart. If you can’t spend on behalf of the Kingdom, you’re not yet ready for abundance.

            PRAYER POINT 
            You have the wisdom to lay down anything for the sake of the Kingdom. You understand the responsibility of wealth and as God multiplies what is upon your life, your heart stays fixed on God as your ultimate treasure. Hallelujah

            The second example is as below

            #IndisputableGeneration
            Friday 29th September 2023

            YOUR DAILY PRAYER IGNITE 
            BY Ap. Samuel Muyita

            Proverbs 4:23 (NIV): "Above all else, guard your heart, for everything you do flows from it."

            GUARDIANS OF THE HEART

            In the treasury of wisdom found in Proverbs, we are given this profound and vital command: "Above all else, guard your heart." It's a directive that carries immense significance because our hearts are the wellspring of our lives, the source from which everything flows.

            Our hearts are not merely the physical organ that pumps blood through our bodies; they are the seat of our emotions, desires, and intentions. Our thoughts, words, and actions all emanate from the condition of our hearts.

            Just as a vigilant guard protects a fortress, we are called to be guardians of our hearts. Why? Because the state of our hearts profoundly impacts the course of our lives. When our hearts are filled with love, compassion, and righteousness, our actions reflect these qualities. Conversely, a heart tainted by bitterness, anger, or envy can lead us down a destructive path.

            In the spiritual journey, guarding our hearts means cultivating a heart that is aligned with God's Word. It means regularly examining our hearts, seeking forgiveness and healing when necessary, and filling our hearts with the love, grace, and truth of Christ.

            So, today, let us pray together:

            PRAYER POINT
            Heavenly Father, we come before you with hearts open and vulnerable. We recognize the importance of guarding our hearts above all else. Please help us to keep our hearts pure and aligned with your will. Grant us the wisdom and discernment to nurture a heart that overflows with love, kindness, and righteousness. May everything we do flow from a heart devoted to you. In Jesus' name, we pray. Amen.

            Please develop your devotion in the similar way the examples were developed
            '''

            devotion_prompt_template = PromptTemplate(
                input_variables=["scripture"],
                template = devotion_prompt,
            )

            llm_chain = LLMChain(llm=llm, prompt=devotion_prompt_template)
            res_devotion = llm_chain.run(verse)

            devotion = Devotion(verse=verse, detail=res_devotion)
            devotion.save()

            return render(request=request, 
                            template_name='tools/devotion.html', 
                            context={'devotion': devotion,
                                     'form': form}
                            )
        else:
            error = 'Invalid form inputs'
            return render(request=request,
                            template_name='tools/devotion.html',
                            context={'form': form, 'error': error}
                            )
    else:
        return render(request=request,
                            template_name='tools/devotion.html',
                            context={'form': form}
                            )
    

def downloadDevotion(request, pk):
    import io
    from reportlab.pdfgen import canvas

    devotion = Devotion.objects.get(pk=pk)

    # Create a PDF file object
    pdf_file = io.BytesIO()

    # Create a PDF canvas object
    canvas = canvas.Canvas(pdf_file)

    # Write the devotion to the PDF canvas
    canvas.setFont("Helvetica", 12)
    canvas.drawString(10, 10, devotion.detail)

    # Close the PDF canvas object
    canvas.showPage()
    canvas.save()

    # Set the response content type and filename
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="devotion.pdf"'

    # Write the PDF file object to the response
    response.write(pdf_file.getvalue())

    # Close the PDF file object
    pdf_file.close()

    return response

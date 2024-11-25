from django.shortcuts import render

from .models import (
    HeaderText,
    FooterText,
    LeftBlock,
    RightBlock,
    MiniBlocks,
    MiniBlock3,
    SevenBlocks,
    QuestionsBlock,
    ContactUs,
    SixBlocks,
    Socials

)    

def index(request):
  context = {
          "header_text": HeaderText.objects.all().first(),
          "footer_text": FooterText.objects.all().first(),
          "left_block": LeftBlock.objects.all().first(),
          "right_block": RightBlock.objects.all().first(),
          "mini_blocks": MiniBlocks.objects.all(),
          "mini_block3": MiniBlock3.objects.all().first(),
          "seven_blocks": SevenBlocks.objects.all(),
          "questions_block": QuestionsBlock.objects.all().first(),
          "contact_us": ContactUs.objects.all().first(),
          "six_blocks": SixBlocks.objects.all(),
          "socials": Socials.objects.all()
          
  }        
  
  return render(request,"home.html", context)


def about(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
        "left_block": LeftBlock.objects.all().first(),
        "contact_us": ContactUs.objects.all().first(),
        "socials": Socials.objects.all()
      
    }
    
    return render(request, "about.html", context)


def contact(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
        "contact_us": ContactUs.objects.all().first(),
        "socials": Socials.objects.all()
     
    }
    return render(request, "contact.html", context)


def services(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
        "seven_blocks": SevenBlocks.objects.all(),
        "contact_us": ContactUs.objects.all().first(),
        "socials": Socials.objects.all()
      
    }
    
    return render(request, "services.html", context)


def frequently_questions(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
        "questions_block": QuestionsBlock.objects.all().first(),
        "contact_us": ContactUs.objects.all().first(),
        "six_blocks": SixBlocks.objects.all(),
        "socials": Socials.objects.all()
     
    }
    return render(request, "frequently_questions.html", context)



def drop_down(request):
    context = {
          "header_text": HeaderText.objects.all().first(),
          "footer_text": FooterText.objects.all().first(),
          "left_block": LeftBlock.objects.all().first(),
          "right_block": RightBlock.objects.all().first(),
          "mini_blocks": MiniBlocks.objects.all(),
          "mini_block3": MiniBlock3.objects.all().first(),
          "seven_blocks": SevenBlocks.objects.all(),
          "questions_block": QuestionsBlock.objects.all().first(),
          "contact_us": ContactUs.objects.all().first(),
          "six_blocks": SixBlocks.objects.all(),
          "socials": Socials.objects.all()
    }
    return render(request, "drop_down.html", context)


def read_more(request, seven_blocks_id):
    
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
        "left_block": LeftBlock.objects.all().first(),
        "contact_us": ContactUs.objects.all().first(),
        "socials": Socials.objects.all(),
        "block": SevenBlocks.objects.get(id=seven_blocks_id)
    }

    return render(request, "read_more.html", context)



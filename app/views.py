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
  
  return render(request,"base.html", context)
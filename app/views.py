from django.shortcuts import render

from .models import (
    HeaderText,
    FooterText,
    LeftBlock,
    RightBlock,
    MiniBlocks,
    MiniBlock3 

)    

def index(request):
  context = {
          "header_text": HeaderText.objects.all().first(),
          "footer_text": FooterText.objects.all().first(),
          "left_block": LeftBlock.objects.all().first(),
          "right_block": RightBlock.objects.all().first(),
          "mini_blocks": MiniBlocks.objects.all(),
          "mini_block3": MiniBlock3.objects.all().first()
  }        
  
  return render(request,"base.html", context)
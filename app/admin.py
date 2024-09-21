from django.contrib import admin

from .models import (
    HeaderText,
    FooterText,
    RightBlock,
    MiniBlocks,
    LeftBlock,
    MiniBlock3,
    SevenBlocks,
    QuestionsBlock,
    ContactUs,
    SixBlocks,
    Socials
 
)

admin.site.register(HeaderText)
admin.site.register(FooterText)
admin.site.register(LeftBlock)
admin.site.register(RightBlock)
admin.site.register(MiniBlocks)
admin.site.register(MiniBlock3)
admin.site.register(SevenBlocks)
admin.site.register(QuestionsBlock)
admin.site.register(ContactUs)
admin.site.register(SixBlocks)
admin.site.register(Socials)



from django.contrib import admin

from .models import (
    HeaderText,
    FooterText,
    RightBlock,
    MiniBlocks,
    LeftBlock,
    MiniBlock3
 
)

admin.site.register(HeaderText)
admin.site.register(FooterText)
admin.site.register(LeftBlock)
admin.site.register(RightBlock)
admin.site.register(MiniBlocks)
admin.site.register(MiniBlock3)

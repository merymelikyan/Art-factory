from django.db import models

class HeaderText (models.Model):
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="header_text", blank=True, null=True)

    def __str__(self):
        return f"{self.title1} {self.title2}"

    class Meta:
        verbose_name = "Header Text"
        verbose_name_plural = "Header Text"
 

class FooterText(models.Model):
    text1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.CharField(max_length=255, blank=True, null=True)
    link_url = models.URLField(max_length=200, blank=True, null=True) 
    link_name = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.text1} {self.text2}"

    class Meta:
        verbose_name = "Footer Text"
        verbose_name_plural = "Footer Text" 


class LeftBlock(models.Model):
    image = models.ImageField(upload_to="left_block", blank=True, null=True)
    title = models.CharField(max_length=255)
    link_url = models.URLField(max_length=200, blank=True, null=True) 
    link_name = models.TextField(max_length=255, blank=True, null=True)
    description1 = models.TextField(max_length=255, blank=True, null=True)
    description2 = models.TextField(max_length=255, blank=True, null=True)
    description3 = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Left Block"
        verbose_name_plural = "Left Block"

             
class RightBlock(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="right-block", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Right Block"
        verbose_name_plural = "Right Block"


 
class MiniBlocks(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="mini-blocks", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Mini Blocks"
        verbose_name_plural = "Mini Blocks"


class MiniBlock3(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.TextField(max_length=255, blank=True, null=True)
    description2 = models.TextField(max_length=255, blank=True, null=True)
    link_name = models.TextField(max_length=255, blank=True, null=True)
    link_url = models.URLField(max_length=200, blank=True, null=True) 
    image = models.ImageField(upload_to="mini-block3", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Mini Block3"
        verbose_name_plural = "Mini Block3"



class SevenBlocks(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="seven-blocks", blank=True, null=True)
    text = models.TextField(max_length=55, blank=True, null=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Seven Blocks"
        verbose_name_plural = "Seven Blocks"


class QuestionsBlock(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Questions Block"
        verbose_name_plural = "Questions Blocks"

 
class ContactUs(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.TextField(max_length=255, blank=True, null=True)
    description2 = models.TextField(max_length=255, blank=True, null=True)
    email_name = models.CharField(max_length=255,blank=True, null=True)
    email_url = models.URLField(max_length=200, blank=True, null=True) 
    contact_name = models.CharField(max_length=255,blank=True, null=True)
    contact_class = models.CharField(max_length=200, blank=True, null=True) 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us" 


class SixBlocks(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.TextField(max_length=255, blank=True, null=True)
    description2 = models.TextField(max_length=255, blank=True, null=True)
    html_class = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Six Blocks"
        verbose_name_plural = "Six Blocks"

class Socials(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=255, blank=True)
    html_class = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"
 
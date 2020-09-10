from django.shortcuts import render,redirect
from .forms import TestForm,UserForm,KarutaForm,FinalTestForm
from .models import TestImage,User,Words,Final_data,Karuta_data,Final_Test
from base64 import b64decode
from io import BytesIO,StringIO
from PIL import Image,ImageDraw,ImageFont
from django.core.files.base import ContentFile
from django.views.generic import TemplateView

def UserInfo(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('test3',)
    else:
        form = UserForm()
    return render(request,'mysite/UserInfo.html',{'form':form})

def TestPage(request):
     LastID = User.objects.order_by('-pk')[:1].values()[0]['id']
     words = Words.objects.all()

     if request.method =='POST':
         form = KarutaForm(request.POST)
         if form.is_valid():
             k_data = form.save(commit=False)
             k_data.user= User(id=LastID)
             k_data.save()
             print("saved")

             form = KarutaForm()
             images = Final_data.objects.order_by('?').filter(user=User(id=LastID))
             return render(request,'mysite/test.html',{'images':images,'words':words,'form':form})
     else:
            form = KarutaForm()
            images = Final_data.objects.order_by('?').filter(user=User(id=LastID))
            return render(request,'mysite/test.html',{'images':images,'words':words,'form':form})

def test3(request):

    LastID = User.objects.order_by('-pk')[:1].values()[0]['id']

    if request.method == 'POST':
        form = TestForm(request.POST)

        if form.is_valid():

            for num in range(15):

                image_name = "image"+str(num)
                image_b64 = request.POST[image_name]
                format, imgstr = image_b64.split(";base64,")
                ext = format.split("/")[-1]
                data = ContentFile(b64decode(imgstr),name=image_name+"_user"+str(LastID)+"."+ext)
                TestImage.objects.create(created_image=data)

                img = Image.open(data)
                img = img.resize((200,250))
                draw = ImageDraw.Draw(img)
                draw.rectangle([(0,0),(200,250)],outline='blue',width=5)
                draw.ellipse([(130,10),(190,70)],outline='blue',width=3)

                printing_word = Words.objects.get(pk=num+1).words
                font = ImageFont.truetype("/System/Library/Fonts/ヒラギノ角ゴシック W0.ttc",40)
                draw.text(xy=(145,25),text=printing_word,fill=(0,0,0),font=font,align="center",direction="ttb",language='ja')

                item = BytesIO()
                img.save(item,format="PNG",quality=100)
                new_data = ContentFile(item.getvalue(),name="new_"+image_name+"_user"+str(LastID)+"."+ext)
                temp = Final_data(user=User(id=LastID),final_images=new_data)
                temp.save()

            return redirect('test')
        else:
            print("form不正解")
            return render(request,'mysite/test3/',{'form':form})
    else:
        form = TestForm()
        return render(request,'mysite/test3.html',{'form':form})

class HundredView(TemplateView):
    template_name = "mysite/hundred.html"

def answer(request):

    LastID = User.objects.order_by('-pk')[:1].values()[0]['id']

    if request.method == 'POST':
        form = FinalTestForm(request.POST)
        print(request.POST)

        if form.is_valid():

            for i in range (15):
                name = "words"+str(i)
                temp = Final_Test(user=User(id=LastID),answer=request.POST[name])
                temp.save()
            return redirect('thankyou',)
    else:
        form = FinalTestForm()
        return render(request,'mysite/answer.html',{'form':form})

class ThankYouView(TemplateView):
    template_name = "mysite/thankyou.html"

# Create your views here.

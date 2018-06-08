# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from time import sleep
from onvif import ONVIFCamera
from cam12presets.models import Cam12pr
def index(request):
    return render(request, 'cameraui/homepage.html')

def cam12(request):
    speed = 0.5
    if request.method == 'POST':
	if request.POST.has_key('save'):
	    speed = request.POST.get('speedreg')
	    mycam = ONVIFCamera('192.168.13.12', 80, 'admin', 'Supervisor')
	    media = mycam.create_media_service()
	    ptz = mycam.create_ptz_service()
	    media_profile = media.GetProfiles()[0];
	    status = ptz.GetStatus({'ProfileToken': media_profile._token})
	    TT = request.POST.get('newtitle')
	    if TT=="default":
		for r in Cam12pr.objects.all():
		    plus=r.id
	        TT="default"+ str(plus+1)
	    b = Cam12pr(title=TT,start_x=status.Position.PanTilt._x,start_y=status.Position.PanTilt._y,start_z=status.Position.Zoom._x)
	    b.save()
        if request.POST.has_key('up'):
	    speed = request.POST.get('speedreg')
	    mycam = ONVIFCamera('192.168.13.12', 80, 'admin', 'Supervisor')
	    media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = float(speed)*0.7
            ptz.ContinuousMove(req)
            sleep(0.3)
	    ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('zoomplus'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.12', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.Zoom._x = float(speed)
            ptz.ContinuousMove(req)
            sleep(0.2)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('zoomminus'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.12', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.Zoom._x = -float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('leftup'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.12', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = (float(speed)*0.7)/2
	    req.Velocity.PanTilt._x = -float(speed)/2
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('rightup'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.12', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = (float(speed)*0.7)/2
	    req.Velocity.PanTilt._x = float(speed)/2
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('left'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.12', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._x = -float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('right'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.12', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._x = float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('leftdown'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.12', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = -(float(speed)*0.7)/2
	    req.Velocity.PanTilt._x = -float(speed)/2
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('down'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.12', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = -(float(speed)*0.7)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('rightdown'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.12', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = -(float(speed)*0.7)/2
	    req.Velocity.PanTilt._x = float(speed)/2
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
    return render(request, 'cameraui/cam12main.html', {'spd': [str(speed)]})

def cam13(request):
    speed = 0.5
    if request.method == 'POST':
	if request.POST.has_key('up'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.13', 8999, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('rightup'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.13', 8999, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = float(speed)
	    req.Velocity.PanTilt._x = float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('leftup'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.13', 8999, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = float(speed)
	    req.Velocity.PanTilt._y = -float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('left'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.13', 8999, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._x = -float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('right'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.13', 8999, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._x = float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('down'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.13', 8999, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = -float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('leftdown'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.13', 8999, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = -float(speed)
	    req.Velocity.PanTilt._x = -float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('rightdown'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.13', 8999, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = -float(speed)
	    req.Velocity.PanTilt._x = float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('zoomplus'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.13', 8999, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.Zoom._x = float(speed)
            ptz.ContinuousMove(req)
            sleep(0.2)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('zoomminus'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.13', 8999, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.Zoom._x = -float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
    return render(request, 'cameraui/cam13main.html', {'spd': [str(speed)]})

def cam14(request):
    speed = 0.5
    if request.method == 'POST':
	if request.POST.has_key('zoomminus'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.14', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.Zoom._x = -float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('zoomplus'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.14', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.Zoom._x = float(speed)
            ptz.ContinuousMove(req)
            sleep(0.2)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('up'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.14', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('down'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.14', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = -float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('left'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.14', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._x = -float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('right'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.14', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._x = float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('rightup'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.14', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = float(speed)
	    req.Velocity.PanTilt._x = float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('leftup'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.14', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = float(speed)
	    req.Velocity.PanTilt._x = -float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('rightdown'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.14', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = -float(speed)
	    req.Velocity.PanTilt._x = float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
	if request.POST.has_key('leftdown'):
            speed = request.POST.get('speedreg')
            mycam = ONVIFCamera('192.168.13.14', 80, 'admin', 'Supervisor')
            media = mycam.create_media_service()
            ptz = mycam.create_ptz_service()
            media_profile = media.GetProfiles()[0];
            req = ptz.create_type('ContinuousMove')
            req.ProfileToken = media_profile._token
            ptz.Stop({'ProfileToken': media_profile._token})
            req.Velocity.PanTilt._y = -float(speed)
	    req.Velocity.PanTilt._x = -float(speed)
            ptz.ContinuousMove(req)
            sleep(0.3)
            ptz.Stop({'ProfileToken': media_profile._token})
    return render(request, 'cameraui/cam14main.html', {'spd': [str(speed)]})

def my_lab(request):
    if request.method == 'GET':
	mycam = ONVIFCamera('192.168.13.12', 80, 'admin', 'Supervisor')
	media = mycam.create_media_service()
	ptz = mycam.create_ptz_service()
	media_profile = media.GetProfiles()[0];
	req = ptz.create_type('GetConfigurations')
	req.ConfigurationToken = media_profile.PTZConfiguration._token
	ptz_configuration_options = ptz.GetConfigurationOptions(req)

	req = ptz.create_type('ContinuousMove')
	req.ProfileToken = media_profile._token
	ptz.Stop({'ProfileToken': media_profile._token})
	status = ptz.GetStatus({'ProfileToken': media_profile._token})
        start_x = status.Position.PanTilt._x
        start_y = status.Position.PanTilt._y
	req.Velocity.Zoom._x = 1
	ptz.ContinuousMove(req)
	sleep(4)
	ptz.Stop({'ProfileToken': req.ProfileToken})
	a=0
        print 'razgon'
	while a < 1:
        	a=a+0.05
        	req.Velocity.PanTilt._x = -a/2
        	req.Velocity.PanTilt._y = -a/2
        	ptz.ContinuousMove(req)
        a = -0.05
    	b = 1.05
    	print 'circle'
    	while a < 1:
        	a = a+0.05
        	b = b - 0.05
        	if ((b<0.05) or (b<0)):
        	        b = 0
        	req.Velocity.PanTilt._x = -b/2-0.1
        	req.Velocity.PanTilt._y = a/2
        	ptz.ContinuousMove(req)
    	a = -0.05
    	b = 1.05
    	while a < 1:
        	a = a+0.05
        	b = b - 0.05
        	if ((b<0.05) or (b<0)):
                	b = 0
        	req.Velocity.PanTilt._x = a/2+0.1
        	req.Velocity.PanTilt._y = b/2
        	ptz.ContinuousMove(req)
    	a = -0.05
    	print 'diag'
    	while a < 1:
        	a = a+0.08
        	req.Velocity.PanTilt._x = 0.5
        	req.Velocity.PanTilt._y = -0.5
        	ptz.ContinuousMove(req)
    	a = -0.05
    	b = 1.05
    	print 'circle'
    	while a < 1:
        	a = a+0.05
        	b = b - 0.05
        	if ((b<0.05) or (b<0)):
                	b = 0
        	req.Velocity.PanTilt._x = b/2+0.1
        	req.Velocity.PanTilt._y = a/2
        	ptz.ContinuousMove(req)
    	a = -0.05
    	b = 1.05
    	while a < 1:
        	a = a+0.05
        	b = b - 0.05
        	if ((b<0.05) or (b<0)):
                	b = 0
        	req.Velocity.PanTilt._x = -a/2-0.1
        	req.Velocity.PanTilt._y = b/2
        	ptz.ContinuousMove(req)
    	print 'tormoz'
    	a = 1.05
	while a > 0:
        	a=a-0.05
       		if ((a<0.5) or (a<0)):
                	a = 0
        	req.Velocity.PanTilt._x = -a/2
        	req.Velocity.PanTilt._y = -a/2
        	ptz.ContinuousMove(req)
	
	ptz.Stop({'ProfileToken': req.ProfileToken})
	req.Velocity.Zoom._x = -1
	ptz.ContinuousMove(req)
	sleep(4)
	ptz.Stop({'ProfileToken': req.ProfileToken})
    return render(request, 'cameraui/homepage.html') 
# Create your views: hee.

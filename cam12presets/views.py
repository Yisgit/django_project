# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from cam12presets.models import Cam12pr
from time import sleep
from onvif import ONVIFCamera
from multiprocessing import Process, Queue
import math

def stata(media_profile, ptz, q,vect,xspeed,yspeed):
    status = ptz.GetStatus({'ProfileToken': media_profile._token})
    x1 = status.Position.PanTilt._x
    y1 = status.Position.PanTilt._y
    cur_x = x1
    cur_y = y1
    contvect = 0
    n=0
    vect = vect*2
    while vect >0:
	status = ptz.GetStatus({'ProfileToken': media_profile._token})
	if status.Position.PanTilt._x != x1 or status.Position.PanTilt._y != y1:
	    prev_x = cur_x
	    prev_y = cur_y
	    cur_x = status.Position.PanTilt._x
	    cur_y = status.Position.PanTilt._y
	    if prev_x == cur_x and prev_y == cur_y:
		n=n+1
		if n ==3:
		    vect = 0
		    print "egggz"
	    else:
		n = 0
	    if cur_y >0:
                if prev_y >0:
                    if prev_y > cur_y:
                        y = -(prev_y - cur_y)
                    elif prev_y < cur_y:
                        y = cur_y - prev_y
                    else:
                        y = 0
                elif prev_y <= 0:
                    y = cur_y - prev_y
            elif cur_y <=0:
                if prev_y >0:
                    y = -(prev_y - cur_y)
                elif prev_y<=0:
                    if prev_y > cur_y:
                        y = prev_y - cur_y
                    elif prev_y <cur_y:
                        y = cur_y - prev_y
                    else:
                        y = 0
	    if (cur_x>= 0.638056) and (cur_x <=1):
                if (prev_x>= 0.638056) and (prev_x <=1):
                    if prev_x>cur_x:
                        x = prev_x-cur_x
                    elif prev_x<cur_x:
                        x = -(cur_x-prev_x)
                    else:
                        x=0
                elif (prev_x>=-1) and (prev_x<=0):
                    if (prev_x == -1) and (cur_x==1):
                        x = 0
                    else:
                        x = (1-cur_x) + (1+prev_x)
                elif (prev_x>=0) and (prev_x<=0.5825):
                    if cur_x==1:
                        x = prev_x+1
                    else:
                        x = prev_x+1+(1-cur_x)
            elif (cur_x<=0) and (cur_x>=-1):
                if (prev_x>= 0.638056) and (prev_x <=1):
                    if (prev_x==1) and (cur_x==-1):
                        x=0
                    else:
                        x = -((1+cur_x)+(1-prev_x))
                elif (prev_x>=-1) and (prev_x<=0):
                    if prev_x==cur_x:
                        x=0
                    elif cur_x<prev_x:
                        x=prev_x-cur_x
                    elif cur_x>prev_x:
                        x=-(cur_x-prev_x)
                elif (prev_x>=0) and (prev_x<=0.5825):
                    if prev_x == cur_x:
                        x=0
                    else:
                        x=prev_x-cur_x
	        elif (prev_x>=0) and (prev_x<=0.5825):
                    if prev_x == cur_x:
                        x=0
                    else:
                        x=prev_x-cur_x
	    elif (cur_x>=0) and (cur_x<=0.5825):
                if (prev_x>= 0.638056) and (prev_x <=1):
                    if prev_x == 1:
                        x = -(cur_x + 1)
                    else:
                        x=-(cur_x+1 +(1-prev_x))
                elif (prev_x>=-1) and (prev_x<=0):
                    if prev_x==cur_x:
                        x=0
                    else:
                        x=-(cur_x-prev_x)
                elif (prev_x>=0) and (prev_x<=0.5825):
                    if prev_x==cur_x:
                        x=0
                    elif prev_x>cur_x:
                        x=prev_x-cur_x
                    elif prev_x<cur_x:
                        x=-(cur_x-prev_x)
	    xmath = math.copysign(x,1)
            ymath = math.copysign(y,1)
            if xmath!=0 and ymath!=0:
                minus_vect = math.sqrt(xmath**2+ymath**2)
            elif xmath==0:
                minus_vect = ymath
            elif ymath==0:
                minus_vect = xmath
            elif xmath==0 and ymath==0:
                minus_vect = 0      
	    l = [minus_vect]
	    print "second trit"+str(cur_x) +"+"+str(cur_y)
	    q.put(l)
	    vect = vect - minus_vect

def moveto(req,ptz,vect,q,xspeed,yspeed,zoom):
    if vect>0.4:
        contvect = 0
	actxspeed = 0
        actyspeed = 0
	while actyspeed !=yspeed:
            actxspeed = actxspeed + xspeed/20
            actyspeed = actyspeed + yspeed/20
	    if xspeed>0:
		if actxspeed > xspeed:
		    actxspeed = xspeed
	    elif xspeed <0:
	        if actxspeed<xspeed:
		    actxspeed = xspeed
	    if yspeed >0:
	        if actyspeed> yspeed:
	            actyspeed = yspeed
	    elif yspeed <0:
		if actyspeed<yspeed:
		    actyspeed=yspeed
	    if math.copysign(xspeed,1)<0.07:
		actxspeed = xspeed*5
            req.Velocity.PanTilt._x = actxspeed
            req.Velocity.PanTilt._y = actyspeed
            ptz.ContinuousMove(req)
	    print "1+"
            cur_stats = q.get()
            vect = vect-cur_stats[0]
	    contvect = contvect + cur_stats[0]	
	vect = vect-contvect*1.9
	while vect>0:
	    print xspeed
	    req.Velocity.PanTilt._x = actxspeed
	    req.Velocity.PanTilt._y = yspeed
	    ptz.ContinuousMove(req)
	    print "2+"
	    cur_stats = q.get()
	    vect = vect - cur_stats[0]
	while actyspeed !=0:
	    actxspeed = actxspeed - xspeed/20
	    actyspeed = actyspeed - yspeed/20
	    if xspeed >0:
		if actxspeed <xspeed/20:
		    actxspeed = 0
	    elif xspeed <0:
		if actxspeed > xspeed/20:
		    actxspeed=0
	    if yspeed>0:
		if actyspeed < yspeed/20:
		    actyspeed = 0
	    elif yspeed<0:
		if actyspeed>yspeed/20:
		    actyspeed=0
	    req.Velocity.PanTilt._x = actxspeed
	    req.Velocity.PanTilt._y = actyspeed
	    ptz.ContinuousMove(req)
	    print "3+"
	ptz.Stop({'ProfileToken':req.ProfileToken})
	abbbs=ptz.create_type('AbsoluteMove')
        abbbs.ProfileToken=req.ProfileToken
        abbbs.Position.Zoom._x=zoom
        ptz.AbsoluteMove(abbbs)


def preset_view(request, BD = Cam12pr):
    if request.method == 'POST':
	if request.POST.has_key('GoTo'):
	    if request.POST.get('choice'):
	        q=request.POST.get('choice')
		start_x = Cam12pr.objects.get(id=int(q)).start_x
		start_y = Cam12pr.objects.get(id=int(q)).start_y
		zoom = Cam12pr.objects.get(id=int(q)).start_z
		mycam = ONVIFCamera('192.168.13.12', 80, 'admin', 'Supervisor')
		media = mycam.create_media_service()
		ptz = mycam.create_ptz_service()
		media_profile = media.GetProfiles()[0];
		req = ptz.create_type('GetConfigurationOptions')
    		req.ConfigurationToken = media_profile.PTZConfiguration._token
    		ptz_configuration_options = ptz.GetConfigurationOptions(req)
    		req = ptz.create_type('ContinuousMove')
    		req.ProfileToken = media_profile._token
    		ptz.Stop({'ProfileToken': media_profile._token})
		status = ptz.GetStatus({'ProfileToken': media_profile._token})
		cur_x = status.Position.PanTilt._x
		cur_y = status.Position.PanTilt._y
		if cur_y >0:
        	    if start_y >0:
            		if start_y > cur_y:
                	    y = -(start_y - cur_y)
            		elif start_y < cur_y:
                	    y = cur_y - start_y
            		else:
                	    y = 0
        	    elif start_y <= 0:
            		y = cur_y - start_y
    		elif cur_y <=0:
        	    if start_y >0:
            		y = -(start_y - cur_y)
        	    elif start_y<=0:
            		if start_y > cur_y:
                	    y = -(start_y - cur_y)
            		elif start_y <cur_y:
                	    y = cur_y - start_y
            		else:
                	    y = 0
		if (cur_x>= 0.638056) and (cur_x <=1):
		    if (start_x>= 0.638056) and (start_x <=1):
            		if start_x>cur_x:
                	    x = start_x-cur_x
            	    	elif start_x<cur_x:
                	    x = -(cur_x-start_x)
            	    	else:
                	    x=0
        	    elif (start_x>=-1) and (start_x<=0):
            		if (start_x == -1) and (cur_x==1):
                	    x = 0
            		else:
                	    x = (1-cur_x) + (1+start_x)
        	    elif (start_x>=0) and (start_x<=0.5825):
            		if cur_x==1:
                	    x = start_x+1
            		else:
                	    x = start_x+1+(1-cur_x)
    		elif (cur_x<=0) and (cur_x>=-1):
        	    if (start_x>= 0.638056) and (start_x <=1):
            		if (start_x==1) and (cur_x==-1):
                	    x=0
            		else:
               		    x = -((1+cur_x)+(1-start_x))
        	    elif (start_x>=-1) and (start_x<=0):
            		if start_x==cur_x:
                	    x=0
            		elif cur_x<start_x:
                	    x=start_x-cur_x
            		elif cur_x>start_x:
                	    x=-(cur_x-start_x)
        	    elif (start_x>=0) and (start_x<=0.5825):
            		if start_x == cur_x:
                	    x=0
            		else:
                	    x=start_x-cur_x
    		elif (cur_x>=0) and (cur_x<=0.5825):
        	    if (start_x>= 0.638056) and (start_x <=1):
            		if start_x == 1:
                	    x = -(cur_x + 1)
            		else:
                	    x=-(cur_x+1 +(1-start_x))
        	    elif (start_x>=-1) and (start_x<=0):
            		if start_x==cur_x:
                	    x=0
            		else:
                	    x=-(cur_x-start_x)
        	    elif (start_x>=0) and (start_x<=0.5825):
            		if start_x==cur_x:
                	    x=0
            	    	elif start_x>cur_x:
                	    x=start_x-cur_x
            	    	elif start_x<cur_x:
                	    x=-(cur_x-start_x)
		xmath = math.copysign(x,1)
		ymath = math.copysign(y,1)
		vect = math.sqrt(xmath**2+ymath**2)
		if math.copysign(x,1)>math.copysign(y,1):
                    #xspeed = math.copysign(0.5*1.997,x)
	 	    xspeed = math.copysign(0.8,x)
       		    #yspeed = round(math.copysign(0.736/xmath*ymath,y),6)
		    yspeed = round(math.copysign(0.8*ymath/xmath*0.7,y),6)
    	  	elif math.copysign(x,1)<math.copysign(y,1):
        	    #yspeed = math.copysign(0.5*0.9,y)
		    yspeed = math.copysign(0.8*0.7,y)
        	    xspeed = math.copysign(1*xmath/ymath,x)
	   	    #xspeed = round(math.copysign(2.5*1*xmath/ymath,x),6)
		print xspeed
		print yspeed
		q = Queue()
		process_stata = Process(target=stata, args=(media_profile, ptz, q,vect,xspeed,yspeed))
		process_cam = Process(target=moveto, args=(req,ptz,vect,q,xspeed,yspeed,zoom))
		process_cam.start()
		process_stata.start()
		q.close()
		q.join_thread()
		process_cam.join()
		process_stata.join()
    l = []	
    for R in Cam12pr.objects.all():
	l.append(R)
    return render(request, 'cam12presets/cam12presets.html', {'obj_list': l})
# Create your views here.

#! /usr/bin/env python3.8
import rospy # rospy projeye dahil edildi
from std_msgs.msg import String # mesaj için gerekli kütüphane

if __name__ == '__main__' :
 rospy.init_node('composiv_talker')
 pub = rospy.Publisher("/mytopic", String, queue_size=10 ) # topic adı ve #mesaj tipi ve buffer boyutu ayarlandı
 
 rate = rospy.Rate(2) #rate tanımlandı
 while not rospy.is_shutdown(): #durdurulmadığı sürece çalış
  msg = String() #mesaj tipi String
  msg.data ="Merhaba, Ben Kadir" #yayınlanan mesaj
  pub.publish(msg) #yayaınla işlemi
  rate.sleep() #beklet
  
 rospy.loginfo("Node stopped") #durduğunda verşlecek mesaj
 

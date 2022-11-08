#! /usr/bin/env python3.8
import rospy # rospy projeye dahil edildi
from std_msgs.msg import String # mesaj için gerekli kütüphane

def callback_listener_data(msg): #mesaj geldiğince çalışacak fonksiyon
 rospy.loginfo("Mesaj Alındı : ") #bilgi mesajı
 rospy.loginfo(msg)

if __name__ == '__main__' :
 rospy.init_node('composiv_listener') # init_node ile node başlatıldı
 sub = rospy.Subscriber("/mytopic",String,callback_listener_data) #içerisine #topic adı mesaj tipi ve fonksiyon verildi
 rospy.spin() #mesaj geldikçe dön

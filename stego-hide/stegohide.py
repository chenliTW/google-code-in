#! /usr/bin/python3
import sys,cv2

def gcd(a,b):
  while b:
    temp=a%b
    a=b
    b=temp
  return a

def hide_text(image, text):
  encoded_message=[]
  for  i in text:
    encoded_message.append(ord(i))
  hide_point = gcd(len(image), len(image[0]))
  encode_index=0
  for i in range(len(image)):
    for j in range(len(image[0])):
      if (i+1 * j+1) % hide_point == 0:
        image[i-1][j-1][0] = encoded_message[encode_index]
        encode_index+=1
        if encode_index==len(encoded_message):
          return image

def decode_image(image):
  decode_point = gcd(len(image), len(image[0]))
  secret_message = ''
  for i in range(len(image)):
    for j in range(len(image[0])):
      if (i-1 * j-1) % decode_point == 0:
        if image[i-1][j-1][0] != 0:
          secret_message = secret_message + chr(image[i-1][j-1][0])
        else:
          return secret_message

if __name__=="__main__":
  if len(sys.argv)!=3:
    print("usuage: ./stegohide.py [-e (encode)/-d (decode)] [image_path]")
    exit(0)
  try:
   image=cv2.imread(sys.argv[2])
  except:
    print("image open error!!")
    exit(0)
  if sys.argv[1]=="-e":
    text=input("Enter a message to hide:")
    cv2.imwrite(sys.argv[2], hide_text(image,text))
  elif sys.argv[1]=="-d":
    print(decode_image(image))
  else:
    print("usuage: ./stegohide.py [-e (encode)/-d (decode)] [image_path]")
    exit(0)
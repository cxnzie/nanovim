import sys
f=''
b=[]
print('~ NANOVIM ~\nCommands: :w=save :q=quit')
try:
 while 1:
  try:t=input(f'{":" if not b else " "}{len(b)+1}')
  except EOFError:break
  if t==':q':break
  if t==':w':
   try:f=input('File: ');open(f,'w').write('\n'.join(b));print(f"'{f}' saved")
   except:print('E212: Can\'t save file')
  else:b+=[t]
except KeyboardInterrupt:pass
print('bye')

import os
b=[]
f=''
print('~ NANOVIM ~\nType text, use :w to save, :q to quit, :wq to save and quit')
try:
 while 1:
  t=input('> ')
  if t==':q':break
  if t==':wq':
   if not f:f=input('File: ')
   if f:open(f,'w').write('\n'.join(b))
   break
  if t==':w':
   if not f:f=input('File: ')
   if f:
    open(f,'w').write('\n'.join(b))
    print(f"Saved '{f}'")
  else:b+=[t]
except (KeyboardInterrupt,EOFError):pass
print('Bye!')

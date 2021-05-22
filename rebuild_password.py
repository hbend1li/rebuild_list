#!/usr/bin/env python3
import argparse
import time
import keyboard

parser = argparse.ArgumentParser()
parser.add_argument("password_file", help="new password list to add.")

args = parser.parse_args()

start_time = time.time()
pw = 0
pw_add = 0

# Open a file
file_src = open(args.password_file, 'r')
new_wordlist = list(file_src)
new_lines = len(new_wordlist)

file_dst = open('wordlist.txt', 'r+')
wordlist = list(file_dst)

new_pass = list()

print("[%d] password ready to check, press 'ESC' to exit."%new_lines)

for line in new_wordlist:
  pw = pw + 1
  ln = pw*100/new_lines
  line = line.replace('\r', '').replace('\n', '')
  
  print("  [%.1f%%, %dpwd, +%d] %s                                " %(ln,pw,pw_add,line), end ="\r")
  
  Found = False
  for line_wordlist in wordlist:
    line_wordlist = line_wordlist.replace('\r', '').replace('\n', '')
    if line == line_wordlist:
      Found = True
      break

  if not Found:
    for line_new_pass in new_pass:
      if line == line_new_pass:
        Found = True
        break

  if not Found:
    new_pass.append(line)
    #print ("+ %s                                    " % line)
    pw_add = pw_add+1

  if keyboard.is_pressed('esc'):
    break

# save 
file_src.close()
new_pass=map(lambda x:x+'\n', new_pass)
file_dst.writelines(new_pass)
file_dst.close()
print("\r\nTolal [%d/%d] password saved to 'wordlist.txt' in [%.3f]s" %(pw_add,new_lines,(time.time() - start_time)))

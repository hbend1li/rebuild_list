#!/usr/bin/env python3
import argparse
import time
#import keyboard

parser = argparse.ArgumentParser()
parser.add_argument("List1", help="source list.")
parser.add_argument("List2", help="destination list.")

args = parser.parse_args()
start_time = time.time()
word = 0
word_added = 0

# Open a file
file_src = open(args.List1, 'r')
new_wordlist = list(file_src)
new_lines = len(new_wordlist)

file_dst = open(args.List2, 'r+')
wordlist = list(file_dst)

new_list = list()

print("[%d] password ready to check, press 'ESC' to exit."%new_lines)

for line in new_wordlist:
  word = word + 1
  ln = word*100/new_lines
  line = line.replace('\r', '').replace('\n', '')
  
  print("  [%.1f%%, %dpwd, +%d] %s                                " %(ln,pw,pw_add,line), end ="\r")
  
  Found = False
  for line_wordlist in wordlist:
    line_wordlist = line_wordlist.replace('\r', '').replace('\n', '')
    if line == line_wordlist:
      Found = True
      break

  if not Found:
    for line_new_pass in new_list:
      if line == line_new_pass:
        Found = True
        break

  if not Found:
    new_list.append(line)
    #print ("+ %s                                    " % line)
    word_added = word_added+1

  # if keyboard.is_pressed('esc'):
  #   break

# save 
file_src.close()
new_list=map(lambda x:x+'\n', new_list)
file_dst.writelines(new_list)
file_dst.close()
print("\r\nTolal [%d/%d] word saved to '%s' in [%.3f]s" %(word_added,new_lines,args.List2,(time.time() - start_time)))

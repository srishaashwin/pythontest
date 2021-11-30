{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f550ea3f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "def odd_even(a):\n",
      "    if(a%2==0):\n",
      "        print(\"the numb is even\")\n",
      "    else:\n",
      "        print(\"the numb is odd\")\n",
      "\n",
      "        \n",
      "        \n",
      "def palan(b):\n",
      "    if(b==b[::-1]):\n",
      "        print(\"palandrome\")\n",
      "    else:\n",
      "        print(\"not palandrome\")\n",
      "-----------\n",
      "232\n",
      "15\n",
      "-----------\n",
      ":\n",
      "    if(a%2==0):\n",
      "        print(\"the numb is even\")\n",
      "    else:\n",
      "        print(\"the numb is odd\")\n",
      "\n",
      "        \n",
      "        \n",
      "def palan(b):\n",
      "    if(b==b[::-1]):\n",
      "        print(\"palandrome\")\n",
      "    else:\n",
      "        print(\"not palandrome\")\n",
      "-----------\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#  Read mode\n",
    "#cursour in index 0\n",
    "\n",
    "f=open(\"myown.py\",\"r\")\n",
    "print(f.tell())\n",
    "print(f.read())\n",
    "print(\"-----------\")\n",
    "\n",
    "print(f.tell())\n",
    "print(f.seek(15))### moves the cursor to index15 \n",
    "print(\"-----------\")\n",
    "print(f.read())###### prints the entire txt after index15\n",
    "print(\"-----------\")\n",
    "print(f.read())#### empty string will be printed bcz ther is nothing to read after end"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3a737358",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "19\n",
      "29\n"
     ]
    }
   ],
   "source": [
    "# Write mode\n",
    "\n",
    "\n",
    "#(if the file present so it will delete the content of file )\n",
    "\n",
    "#here iam using write mode and writing inbetween the txt \n",
    "#and at the end of the txt\n",
    "f= open(\"write1\",'w')# file is created\n",
    "print(f.tell())\n",
    "f.write(\"iam inside the file\")\n",
    "print(f.tell())\n",
    "f.seek(3)\n",
    "f.write(\"#####iam inserted herer###\")# over written\n",
    "print(f.tell())\n",
    "f.write(\"    pls check me   \")#added at the end\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "1a4076fd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "38\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "# Append mode\n",
    "\n",
    "\n",
    "f=open(\"append1\",'a')##creating a file \n",
    "print(f.tell())##finding cursor loc\n",
    "f.write(\"this is append mode\")\n",
    "f.seek(5)#### seek wont have any impact\n",
    "print(f.tell())\n",
    "f.write(\"checking for append\")# even u do seek it willonly be inserted in end\n",
    "\n",
    "f.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "ce0ea549",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22\n",
      "this is write read\n",
      "hii this ichecking for index 10 insertion\n"
     ]
    }
   ],
   "source": [
    "# Write and read mode  \"w+\"(write is dominent)\n",
    "\n",
    "#if file exist then it will delete the contents in file\n",
    "\n",
    "f=open(\"write-read\",\"w+\")#creating file\n",
    "f.write(\"hii this is write read\")\n",
    "print(f.tell())\n",
    "f.seek(4)###### reading from the index 4\n",
    "print(f.read())\n",
    "f.seek(10)\n",
    "f.write(\"checking for index 10 insertion\")##ower writing the txt from index10\n",
    "f.seek(0)\n",
    "print(f.read())\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "353271cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this is my read+\n",
      "    if(a%2==0):\n",
      "        print(\"the numb is even\")\n",
      "    else:\n",
      "        print(\"the numb is odd\")\n",
      "\n",
      "        \n",
      "        \n",
      "def palan(b):\n",
      "    if(b==b[::-1]):\n",
      "        print(\"palandrome\")\n",
      "    else:\n",
      "        print(\"not palandrome\")\n",
      "_____________________________\n",
      "0\n",
      "this is my read+\n",
      "    if(a%2==0):\n",
      "        print(\"the numb is even\")\n",
      "    else:\n",
      "        print(\"the numb is odd\")\n",
      "\n",
      "        \n",
      "        \n",
      "def palan(b):\n",
      "    if(b==b[::-1]):\n",
      "        print(\"palandrome\")\n",
      "    else:\n",
      "        print(\"not palandrome\")\n"
     ]
    }
   ],
   "source": [
    "#Read and Write mode \"r+\"(read is dominent)\n",
    "# if no file we get error\n",
    "\n",
    "f=open(\"myown.py\",\"r+\")\n",
    "print(f.read())\n",
    "f.seek(0)\n",
    "print(\"_____________________________\")\n",
    "f.write(\"this is my read+\")\n",
    "f.seek(0)\n",
    "print(f.tell())\n",
    "print(f.read())\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "4949b718",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this is a append read modethis is a append read modethis is a append read modethis is a append read mode\n",
      "this is a append read modethis is a append read modethis is a append read modethis is a append read modeiam tying to insert in index 0\n"
     ]
    }
   ],
   "source": [
    "# Append and read mode( seek wont have any impact)\n",
    "\n",
    "# i have executed many times so printed many times\n",
    "\n",
    "f=open(\"appendread\",\"a+\")\n",
    "f.write(\"this is a append read mode\")\n",
    "f.seek(0)\n",
    "print(f.read())#only for read seek works\n",
    "f.seek(0)#  seek wont work for write function\n",
    "f.write(\"iam tying to insert in index 0\")##### but appended at the end\n",
    "f.seek(0)\n",
    "print(f.read())\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "f8c0f0c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hii this is for task\n",
      "the task s for file handling\n",
      "file handling workning \n",
      "workning technique\n",
      "______________________________\n",
      "['hii', 'this', 'is', 'for', 'task', 'the', 'task', 's', 'for', 'file', 'handling', 'file', 'handling', 'workning', 'workning', 'technique']\n",
      "______________________________\n",
      "92\n",
      "16\n",
      "4\n",
      "handling\n",
      "handling\n",
      "workning\n",
      "workning\n",
      "technique\n"
     ]
    }
   ],
   "source": [
    "#read a txt file\n",
    "#count no of characters , words and lines from the file\n",
    "# return all the words whose length is more than 6\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "with open(\"task.txt\",'r') as f:\n",
    "    print(f.read())\n",
    "    print(\"______________________________\")\n",
    "    f.seek(0)\n",
    "    charno= len(f.read())\n",
    "    f.seek(0)\n",
    "    words=f.read().split()\n",
    "    print(words)\n",
    "    print(\"______________________________\")\n",
    "\n",
    "    f.seek(0)\n",
    "    line=len(f.readlines())\n",
    "    print(charno)\n",
    "    print(len(words))\n",
    "    print(line)\n",
    "    f.seek(0)\n",
    "    for i in words:\n",
    "        if(len(i)>6):\n",
    "            print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "aed4baf3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# open a image with jpg format and copy the content in that to another png file\n",
    "\n",
    "\n",
    "\n",
    "with open(\"python.jpg\",\"rb\") as f1:# read binary mode\n",
    "    with open(\"copypython.png\",\"wb\")as f2:# write binary mode\n",
    "        f2.write(f1.read())# writing the in to f2 by reading f1 in f2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "620634a7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

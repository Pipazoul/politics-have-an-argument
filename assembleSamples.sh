# bin/bash

# Usage sh assembleSamples.sh path/to/files MyFileName.mp3
input=$1
outputName=$2

# with a bash for loop
for f in $input/*.mp3; do 
    echo "file '$f'" >> mylist.txt; 
    echo "file 'silence(3s).mp3'" >> mylist.txt;
    done
# or with printf
#printf "file '%s'\n" $input/*.mp3 > mylist.txt
ffmpeg -f concat -safe 0 -i mylist.txt -c copy data_send/$outputName
#rm mylist.txt
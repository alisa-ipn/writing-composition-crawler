ls *.txt | while read f; do 
  fbase=$(basename $f); 
  fbase_no_ext=${fbase%.*}; 
  fout=${fbase_no_ext}"_lined.txt";
  echo -e $fout; 
  perl sentence_boundary.pl -d HONORIFICS -i $f -o output_file ;
done



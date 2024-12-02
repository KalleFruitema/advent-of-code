if [ $# -eq 0 ]
then
  echo "Enter year: "
  read year
else
  year="$1"
fi

mkdir $year
cd $year
for i in {01..25}
do
  mkdir "day_$i"
  cd "day_$i"
  touch input.txt test_input.txt
  for y in {1..2}
  do
    echo -e "import numpy as np\nfrom useful import *\n\n\nwith open(\"2024/day_$i/test_input.txt\") as file:\n    data = [line.strip() for line in file]\n" > "part_$y.py"
  done
  cd ..
done

# Create data1.txt with numbers from 1 to 10

for i in {1..10};
do
    let j=i+1
    echo $i $j >> data1.txt
done
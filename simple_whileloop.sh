# A sample while loop

count=0

while [ $count -lt 10 ];
do
    echo The counter is at $count
    let count=count+2
done
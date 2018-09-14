pyRad7="/home/pi/Soft/monitoringSystem/rad7/rad7_test.py"
waitTime=5000

while :
do
        $pyRad7 > outRad7.dat
	echo "Press [CTRL+C] to stop.."
	sleep $waitTime
done

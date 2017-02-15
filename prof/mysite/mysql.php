<?php
$servername = "216.219.81.80";
$username = "dustin_attendance";
$password = "32M1w9dIgw";
$dbname = "dustin_lookingforward";

$student_system_id = -1;
$class_system_id = -1;
$prof_system_id = -1;
$attendance_record_system_id = -1;

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check what the script should be doing based on the func variable
$func = htmlspecialchars($_POST["func"]);

if($func == 1){// Update student attendance
	// Get HTML GET info
	$class_name = htmlspecialchars($_POST["class"]);
	$prof_username = htmlspecialchars($_POST["prof"]);
	$day = htmlspecialchars($_POST["day"]);
	$student_id = htmlspecialchars($_POST["student"]);

	// 1. Let's get the prof system ID to make sure we are only check that prof's records
	$prof_query = "SELECT id FROM auth_user WHERE username='" . $prof_username . "'";
	
	if($result = $conn->query($prof_query)){
		$row = $result->fetch_row();
		$prof_system_id = $row[0];
	}
	

	// 2. Check to see if student exists.  If so, save system id so we can properly update database
	$student_query = "SELECT id FROM prof_student WHERE Student_ID_Number=" . $student_id;
	
	if($result1 = $conn->query($student_query)){
		$row = $result1->fetch_row();
		$student_system_id = $row[0];
	}

	// 3. Now that we have the student system ID, let's get the class system ID
	$class_query = "SELECT id FROM prof_class WHERE Class_Name='" . $class_name . "' AND Professor_id=" . $prof_system_id;
	if($result2 = $conn->query($class_query)){
		$row = $result2->fetch_row();
		$class_system_id = $row[0];
	}

	// 4. Now that we have the class_system_id, student_system_id, and prof_system_id, let's update the attendance record to count the student present
	 //4a. First, we need to find the attendance record's system id.
	$attendance_record_query = "SELECT id FROM prof_attendancerecord WHERE Date='" . $day . "' AND Associated_Class_id =" . $class_system_id;

	if($result3 = $conn->query($attendance_record_query)){
		$row = $result3->fetch_row();
		$attendance_record_system_id = $row[0];
	}

	//4b. Finally, lets update the student's attendance by adding them to the present list.
	$update_attendance_query = "INSERT INTO prof_attendancerecord_Present_Students (attendancerecord_id, student_id) VALUES (" . $attendance_record_system_id . ", " . $student_system_id . ")";
	if($result4 = $conn->query($update_attendance_query)){
	}
	
	
}else if($func == 2){// This is for getting a student's attedance information
	// Get POST Variable information
	$class_name = htmlspecialchars($_POST["class"]);
	$prof_username = htmlspecialchars($_POST["prof"]);
	$student_id = htmlspecialchars($_POST["student"]);
	$start_date = htmlspecialchars($_POST["startdate"]);
	$end_date = htmlspecialchars($_POST["enddate"]);
		
	// 1. Let's get the prof system ID to make sure we are only check that prof's records
	$prof_query = "SELECT id FROM auth_user WHERE username='" . $prof_username . "'";
	
	if($result = $conn->query($prof_query)){
		$row = $result->fetch_row();
		$prof_system_id = $row[0];
	}
	

	// 2. Check to see if student exists.  If so, save system id so we can properly update database
	$student_query = "SELECT id FROM prof_student WHERE Student_ID_Number=" . $student_id;
	
	if($result1 = $conn->query($student_query)){
		$row = $result1->fetch_row();
		$student_system_id = $row[0];
	}

	// 3. Now that we have the student system ID, let's get the class system ID
	$class_query = "SELECT id FROM prof_class WHERE Class_Name='" . $class_name . "' AND Professor_id=" . $prof_system_id;
	if($result2 = $conn->query($class_query)){
		$row = $result2->fetch_row();
		$class_system_id = $row[0];
	}

	// 4. Now we need to get all the attendance record ids that belong to the class and that are within the date range
	$attendance_record_query = "SELECT id, Date FROM prof_attendancerecord WHERE Associated_Class_id=" . $class_system_id . " AND Date BETWEEN '" . $start_date . "' AND '" . $end_date . "'";
	$attendance_record_ids = array();
	$attendance_record_dates = array();
	$i = 0;
	$y = 0;
	if($result3 = $conn->query($attendance_record_query)){
		while($row = $result3->fetch_object()){
			foreach ($row as $r){
				if($i % 2 == 0 || $i == 0){
					$attendance_record_ids[$i] = $r;
				}else{
					$attendance_record_dates[$y] = $r;
					$y = $y + 1;
				}
				$i = $i + 1;
			}
		}
	}
	//5. Check to see if the student attended according to the attendance records in $attendance_record_ids
	$j = 0;
	$classes_attended = array();
	foreach ($attendance_record_ids as $ar){
		$check_attendance_query = "SELECT attendancerecord_id from prof_attendancerecord_Present_Students WHERE attendancerecord_id=" . $ar . " AND student_id=" . $student_system_id;
		if($result4 = $conn->query($check_attendance_query)){
			$row = $result4->fetch_row();
			if($row[0] == $ar){
				$classes_attended[$j] = 1;
			}else{
				$classes_attended[$j] = 0;
			}
			$j = $j + 1;
		}
		
	}

	//6. Encode JSON Results for Android Application to Receive
	$data = array();
	$m = 0;
	foreach($classes_attended as $attended){
		if($attended == 1){
			$data[$attendance_record_dates[$m]] = "Present";
		}else{
			$data[$attendance_record_dates[$m]] = "Absent";
		}
		$m = $m + 1;
	}
	header('Content-Type: application/json');
	$json = json_encode($data);
	echo $json;
}

$conn->close();
?>

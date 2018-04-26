<?php 

$output = exec('python testols.py');
// $output = shell_exec('/usr/bin/python testols.py');
print_r($output);

// $command = escapeshellcmd('testols.py');
// $output = shell_exec($command);
// echo $output;

$dir          = './img';
$file_display = array(
    'jpg',
    'jpeg',
    'png',
    'gif'
);

if (file_exists($dir) == false) {
    // echo "Directory \''. $dir. '\' not found!";
} else {
    $dir_contents = scandir($dir);

    foreach ($dir_contents as $file) {
        $exploded = explode('.', $file);
        $file_type = strtolower(end($exploded));
        if ($file !== '.' && $file !== '..' && in_array($file_type, $file_display) == true) {
            // echo '<img src="'. $dir. '/'. $file. '" alt="'. $file. $file, '" />';
        }
    }
}

?>
use std::fs;

fn main() {
    let mut sonar_data = Vec::<i32>::new();
    let filename = "data";
    let mut increases: i32 = 0;

    //Read file by line
    if let Ok(file) = fs::read_to_string(filename) {
        let mut buffer = file.lines();
        while let Some(line) = buffer.next() {
            sonar_data.push(line.parse::<i32>().unwrap());
        }
    } else {
        println!("File not found");
        return;
    }

    //Find the number of times the data increases in sets of 3
    for i in 0..sonar_data.len()-3 {
        if sonar_data[i] < sonar_data[i+3] {
            increases += 1;
        }
    }
    println!("{}", increases);
}

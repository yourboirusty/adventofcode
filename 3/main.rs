use std::fs;

fn main() {
    let filename = "input";
    let mut _length = 12;

    let mut diagnostic_data = vec![0; _length+1];

        
    if let Ok(file) = fs::read_to_string(filename) {
        let mut buffer = file.lines();
        while let Some(line) = buffer.next() {
            for (i, c) in line.chars().enumerate() {
                if c == '0' {
                    diagnostic_data[i] -= 1;
                }
                else {
                    diagnostic_data[i] += 1;
                }
            }
        }
    } else {
        println!("File not found");
        return;
    }


    let mut gamma_str = String::new();
    let mut delta_str = String::new();

    for i in 0.._length {
        if diagnostic_data[i] > 0 {
            gamma_str += "1";
            delta_str += "0";
        }
        else {
            gamma_str += "0";
            delta_str += "1";
        }
    }
    println!("Gamma str: {}", gamma_str);
    println!("Delta str: {}", delta_str);

    let gamma_rate = i32::from_str_radix(&gamma_str, 2).unwrap();
    let delta_rate = i32::from_str_radix(&delta_str, 2).unwrap();

    println!("Gamma rate: {}", gamma_rate);
    println!("Delta rate: {}", delta_rate);
    println!("Rate: {}", gamma_rate * delta_rate);
}
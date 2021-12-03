use std::fs;

struct Position {
    x: i32,
    y: i32,
    aim: i32,
}

fn main(){
    let filename = "input";
    let mut position = Position { x: 0, y: 0, aim: 0 };
    if let Ok(file) = fs::read_to_string(filename) {
        let mut buffer = file.lines();
        while let Some(line) = buffer.next() {
            let mut position_str = line.split(" ").collect::<Vec<&str>>();
                let direction = position_str.remove(0);
                let distance = position_str.remove(0);
                match direction.as_ref() {
                    "forward" => {
                        position.x += distance.parse::<i32>().unwrap();
                        position.y += distance.parse::<i32>().unwrap() * position.aim
                    },
                    "backward" => position.x -= distance.parse::<i32>().unwrap(),
                    "up" => position.aim -= distance.parse::<i32>().unwrap(),
                    "down" => position.aim += distance.parse::<i32>().unwrap(),
                    _ => println!("Unknown direction: {}", direction),
                }
        }
    } else {
        println!("File not found");
        return;
    }

    println!("{} {} = {}", position.x, position.y, position.x*position.y);
}
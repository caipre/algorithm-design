use std::io::prelude::*;
use std::io::{BufReader};
use std::fs::File;

fn main() {
    let mut is = Vec::with_capacity(100_000);

    let f = File::open("./.data").unwrap();
    let reader = BufReader::new(f);
    for line in reader.lines() {
        let line = line.unwrap();
        is.push(line.parse::<usize>().unwrap());
    }

    let mut invs = 0 as usize;
    for i in 0..is.len() {
        for j in i..is.len() {
            if is[i] > is[j] {
                invs += 1;
            }
        }
    }

    println!("{}", invs);
}

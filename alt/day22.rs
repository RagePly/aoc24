use std::fs::read_to_string;
use std::collections::{HashMap, HashSet};
use std::convert::TryInto;

const fn gensec(mut sec: i64) -> i64 {
    sec = ((sec << 6) ^ sec) % 16777216;
    sec = ((sec >> 5) ^ sec) % 16777216;
    ((sec << 11) ^ sec) % 16777216
}

fn lastsec(sec: i64, count: i64) -> i64 {
    (0..count).scan(sec, |st,_| { *st = gensec(*st); Some(*st) }).last().unwrap()
}

fn sol1(secs: &[i64]) -> i64 {
    secs.into_iter().map(|s| lastsec(*s, 2000)).sum()
}

fn genprices(mut sec: i64, count: i64) -> Vec<i64> {
    let mut prices = Vec::with_capacity((count+1) as usize);
    prices.push(sec % 10);
    for _ in 0..count {
        sec = gensec(sec);
        prices.push(sec % 10);
    }
    prices
}

fn sol2(secs: &[i64]) -> i64 {
    let mut combs: HashMap<[i64; 4], i64> = HashMap::with_capacity(2000 * secs.len()); // reserve way to much
    for s in secs.into_iter() {
        let prices = genprices(*s,2000);
        let mut visited: HashSet<[i64;4]> = HashSet::with_capacity(2000);
        for w in prices.windows(5) {
            let diffs: [i64; 4] = (&w[1..])
                .into_iter()
                .scan(w[0], |st,s| { let d = s-*st; *st = *s; Some(d) })
                .collect::<Vec<i64>>()
                .try_into().unwrap();
            
            if visited.insert(diffs) {
                *combs.entry(diffs).or_insert(0) += w[4];
            }
        }
    }
    
    combs.values().max().copied().unwrap()
}

use std::thread;
use std::sync::Arc;
use std::ops::Range;

fn get_chains(secs: Arc<[i64]>, r: Range<usize>) -> HashMap<[i64; 4], i64> {
    let mut combs: HashMap<[i64; 4], i64> = HashMap::with_capacity(2000 * secs.len()); // reserve way to much
    for s in secs.get(r).unwrap().into_iter() {
        let prices = genprices(*s,2000);
        let mut visited: HashSet<[i64;4]> = HashSet::with_capacity(2000);
        for w in prices.windows(5) {
            let diffs: [i64; 4] = (&w[1..])
                .into_iter()
                .scan(w[0], |st,s| { let d = s-*st; *st = *s; Some(d) })
                .collect::<Vec<i64>>()
                .try_into().unwrap();
            
            if visited.insert(diffs) {
                *combs.entry(diffs).or_insert(0) += w[4];
            }
        }
    }
    combs
}

fn sol3(secs: &[i64]) -> i64 {
    let copy_secs: Arc<[i64]> = Arc::from(secs);
    let threads = thread::available_parallelism().unwrap().get() - 1;
    let chunk_size = (secs.len() + (threads - secs.len() % threads)) / threads;
    let mut handles = Vec::with_capacity(threads);

    for i in 0..threads {
        let range = if i == threads - 1 {
            i * chunk_size .. secs.len()
        } else {
            i * chunk_size .. (i+1) * chunk_size
        };
        
        let data = copy_secs.clone();
        handles.push(thread::spawn(move || get_chains(data, range))); 
    }

    let mut combs: HashMap<[i64; 4], i64> = HashMap::new();

    for handle in handles.into_iter() {
        let mut res = handle.join().unwrap();
        for (k,v) in res.drain() {
            *combs.entry(k).or_insert(0) += v;
        }
    }

    combs.values().max().copied().unwrap()
}

use std::time::Instant;
fn timed<A,B>(f: impl Fn(A) -> B, a: A) -> (B, f64) {
    let start = Instant::now();
    let res = f(a);
    (res, start.elapsed().as_secs_f64())
}

fn main() {
    let src = read_to_string("input/day22.txt").unwrap();
    let start_secs = src.trim().split("\n").map(|l| l.trim().parse::<i64>().unwrap()).collect::<Vec<_>>();
    println!("Part 1: {:?}", timed(sol1, &start_secs));
    println!("Part 2: {:?}", timed(sol2,&start_secs));
    println!("Part 2; (thread): {:?}", timed(sol3, &start_secs));
}

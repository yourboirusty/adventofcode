from typing import DefaultDict

spawn_rate = 7

def get_input():
    with open('6/input') as f:
        fish = [0 for _ in range(spawn_rate + 2)]
        for char in f.read().split(','):
            fish[int(char)] += 1
    return fish

def spawn_fish(fish):
    spawn_fish = fish[0]
    for idx in range(len(fish)-1):
        fish[idx] = fish[idx+1]
    fish[-1] = spawn_fish
    fish[spawn_rate - 1] += spawn_fish

def part1():
    fish = get_input()
    for _ in range(80):
        spawn_fish(fish)
    return sum(fish)


def part2():
    fish = get_input()
    for _ in range(256):
        spawn_fish(fish)
    return sum(fish)

if __name__ == "__main__":
    print(f'{part1()=}')
    print(f'{part2()=}')
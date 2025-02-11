def jump_game(nums: list) -> bool:
    current=0
    furthest=0
    jump=0

    for i in range(len(nums)-1):
        furthest = max(furthest, i+nums[i])
        print(furthest)

        if i==current:
            jump+=1
            current=furthest

            if current >= len(nums) - 1:
                break
    return jump


nums = [2,3,0,1,4]
print(jump_game(nums))
def main():
    import sys
    input_data = sys.stdin.read().splitlines()
    
    def process_numbers(nums, index, length, acc):
        if index >= length:
            return acc
        n = int(nums[index])
        if n <= 0:
            acc += n ** 4
        return process_numbers(nums, index + 1, length, acc)

    def process_cases(lines, index, total_cases, results):
        if index >= len(lines) or total_cases == 0:
            return results
        try:
            X = int(lines[index])
            nums = lines[index + 1].split()
            if len(nums) != X:
                results.append("-1")
            else:
                results.append(str(process_numbers(nums, 0, X, 0)))
            return process_cases(lines, index + 2, total_cases - 1, results)
        except:
            results.append("-1")
            return results

    N = int(input_data[0])
    output = process_cases(input_data[1:], 0, N, [])
    print("\n".join(output))


if __name__ == "__main__":
    main()

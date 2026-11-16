  #ITS 103 DISCRETE MATHEMATICS ALGORITHMS

print("23 ALGORITHMS DISCRETE MATHEMATICS")

#SEARCHING ALGORITHMS   

def option_one():
    print("LINEAR SEARCH")
    print()

    # LINEAR SEARCHING

    def linear_search(arr, target):
        print(f"Starting linear search for {target}...")
        for i in range(len(arr)):
            print(f"Step {i+1}: Checking index {i}, value = {arr[i]}")
            if arr[i] == target:
                print(f"Match found at index {i}!")
                return i
        print("Reached end of list. Target not found.")
        return -1

    numbers_input = input("Enter numbers separated by spaces: ")
    numbers = [int(x) for x in numbers_input.split()]
    print("Your list:", numbers)

    search_for = int(input("Enter a number to search for: "))
    result = linear_search(numbers, search_for)

    if result != -1:
        print(f"Element {search_for} found at index {result}")
    else:
        print(f"Element {search_for} not found in the list")

def option_two():
    print("=== BINARY SEARCH ===\n")

    def binary_search(arr, target):
        print(f"Searching for: {target}")
        print(f"Array: {arr}\n")

        low = 0
        high = len(arr) - 1
        step = 1

        # Header for steps
        print("{:<6} {:<6} {:<6} {:<6} {:<10}".format("Step", "Low", "High", "Mid", "Value"))
        print("-" * 45)

        while low <= high:
            mid = low + ((high - low) // 2)
            print("{:<6} {:<6} {:<6} {:<6} {:<10}".format(step, low, high, mid, arr[mid]))

            # Show calculation details like in your guide
            print(f"   → mid = {low} + (({high} - {low}) / 2)")
            print(f"   → mid = {low} + ({(high - low)} / 2)")
            print(f"   → mid = {mid}\n")

            if arr[mid] == target:
                print(f"Result: Found {target} at index {mid}")
                return mid
            elif arr[mid] < target:
                print(f"   → {arr[mid]} < {target}, move RIGHT (low = mid + 1)\n")
                low = mid + 1
            else:
                print(f"   → {arr[mid]} > {target}, move LEFT (high = mid - 1)\n")
                high = mid - 1

            step += 1

        print("Result: Target not found.")
        return -1

    # Input handling
    numbers_input = input("Enter numbers separated by spaces (sorted or unsorted): ")
    numbers = [int(x) for x in numbers_input.split()]
    numbers.sort()
    print("\nYour sorted list:", numbers)

    search_for = int(input("Enter a number to search for: "))
    result = binary_search(numbers, search_for)

    if result != -1:
        print(f"\nFinal Output: Element {search_for} found at index {result}")
    else:
        print(f"\nFinal Output: Element {search_for} not found in the list")

def option_three():
    print("\n=== INTERPOLATION SEARCH ===\n")

    def interpolation_search(arr, target):
        print(f"Searching for: {target}")
        print(f"Array: {arr}\n")

        low = 0
        high = len(arr) - 1
        step = 1

        # Header for steps
        print("{:<6} {:<6} {:<6} {:<6} {:<10}".format("Step", "Low", "High", "Pos", "Value"))
        print("-" * 50)

        while low <= high and target >= arr[low] and target <= arr[high]:

            # Prevent division by zero
            if arr[high] == arr[low]:
                if arr[low] == target:
                    print(f"\nResult: Found at index {low}")
                    return low
                break

            # Interpolation formula
            pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

            # Step details
            print("{:<6} {:<6} {:<6} {:<6} {:<10}".format(step, low, high, pos, arr[pos]))
            print(f"   → pos = {low} + (({target} - {arr[low]}) * ({high} - {low})) / ({arr[high]} - {arr[low]})")
            print(f"   → pos = {pos}\n")

            if arr[pos] == target:
                print(f"Result: Found {target} at index {pos}")
                return pos
            elif arr[pos] < target:
                print(f"   → {arr[pos]} < {target}, move RIGHT (low = pos + 1)\n")
                low = pos + 1
            else:
                print(f"   → {arr[pos]} > {target}, move LEFT (high = pos - 1)\n")
                high = pos - 1

            step += 1

        print("Result: Target not found.")
        return -1

    # === User Input Section ===
    numbers_input = input("Enter numbers separated by spaces: ")
    numbers = [int(x) for x in numbers_input.split()]
    numbers.sort()
    print("\nSorted list:", numbers)

    search_for = int(input("Enter number to search: "))
    result = interpolation_search(numbers, search_for)

    if result != -1:
        print(f"\nFinal Output: Element {search_for} found at index {result}")
    else:
        print(f"\nFinal Output: Element {search_for} not found.")

def option_four():
    print("\n=== JUMP SEARCH ===\n")

    import math

    def jump_search(arr, target):
        print(f"Searching for: {target}")
        print(f"Array: {arr}\n")

        n = len(arr)
        step = int(math.sqrt(n))  
        prev = 0
        step_count = 1

        # Jumping phase
        while prev < n and arr[min(step, n) - 1] < target:
            print(f"Step {step_count}: Jump to index {min(step, n) - 1}, value={arr[min(step, n) - 1]}")
            print(f"   → {arr[min(step, n) - 1]} < {target}, continue jumping...\n")
            prev = step
            step += int(math.sqrt(n))
            step_count += 1
            if prev >= n:
                print("Reached end of list. Target not found.")
                return -1

        # Linear search phase
        print(f"Linear search in block starting at index {prev} up to {min(step, n)-1}\n")
        while prev < min(step, n):
            print(f"Checking index {prev}, value={arr[prev]}")
            if arr[prev] == target:
                print(f"Result: Found {target} at index {prev}")
                return prev
            prev += 1

        print("Result: Target not found.")
        return -1

    # === User Input Section ===
    numbers_input = input("Enter numbers separated by spaces (sorted or unsorted): ")
    numbers = [int(x) for x in numbers_input.split()]
    numbers.sort()
    print("\nYour sorted list:", numbers)

    search_for = int(input("Enter a number to search: "))
    result = jump_search(numbers, search_for)

    if result != -1:
        print(f"\nFinal Output: Element {search_for} found at index {result}")
    else:
        print(f"\nFinal Output: Element {search_for} not found in the list")

def option_five():
    print("\n=== EXPONENTIAL SEARCH (Step-by-Step Solution) ===\n")

    # --- Binary Search ---
    def binary_search(arr, target, left, right):
        print("\n--- BINARY SEARCH PHASE ---")
        while left <= right:
            mid = (left + right) // 2
            print(f"L={left}, M={mid}, R={right}, a[M]={arr[mid]}")

            if arr[mid] == target:
                print(f"   ⇒ Solution: {target} found at index {mid}\n")
                return mid
            elif arr[mid] < target:
                print(f"   → {arr[mid]} < {target}, move right")
                left = mid + 1
            else:
                print(f"   → {arr[mid]} > {target}, move left")
                right = mid - 1
        print("   ⇒ Solution: Target not found in binary search range.\n")
        return -1

    # Exponential Search 
    def exponential_search(arr, target):
        print(f"Searching for {target}...\n")

        # Step 0: Check first element
        if arr[0] == target:
            print(f"a[0] = {target} ⇒ Solution: found at position 0\n")
            return 0

        # Doubling phase
        index = 1
        while index < len(arr) and arr[index] < target:
            print(f"a[{index}] = {arr[index]} ⇒ not equal, doubling index")
            index *= 2 

        # Define binary search range
        left = index // 2
        right = min(index, len(arr) - 1)
        print(f"\n{target} lies between a[{left}]={arr[left]} and a[{right}]={arr[right]}\n")

        # Always perform binary search in that range
        return binary_search(arr, target, left, right)

    # User Input 
    numbers_input = input("Enter numbers separated by spaces (sorted or unsorted): ")
    numbers = [int(x) for x in numbers_input.split()]
    numbers.sort()
    print("\nYour sorted list:", numbers)

    search_for = int(input("Enter a number to search for: "))
    result = exponential_search(numbers, search_for)

    # Final Output 
    print("\n=== FINAL RESULT ===")
    if result != -1:
        print(f"Solution: Element {search_for} found at index {result}")
    else:
        print(f"Solution: Element {search_for} not found in the list")
    

def option_six():
    print("\n=== TERNARY SEARCH (Searching) ===\n")

    def ternary_search(arr, key):
        l, r = 0, len(arr) - 1
        step = 1

        print("{:<6} {:<20} {:<20} {:<20}".format("Step", "Range", "m1 (index,value)", "m2 (index,value)"))
        print("-" * 70)

        while l <= r:
            m1 = l + (r - l) // 3
            m2 = r - (r - l) // 3

            print("{:<6} {:<20} {:<20} {:<20}".format(
                step, f"[{l},{r}] ({arr[l]}..{arr[r]})",
                f"{m1},{arr[m1]}", f"{m2},{arr[m2]}"
            ))

            # Check if key is found
            if arr[m1] == key:
                print(f"   → Found {key} at index {m1}\n")
                return m1
            if arr[m2] == key:
                print(f"   → Found {key} at index {m2}\n")
                return m2

            # Decide which region to search
            if key < arr[m1]:
                print(f"   → {key} < {arr[m1]} → Search LEFT region (r = {m1-1})\n")
                r = m1 - 1
            elif key > arr[m2]:
                print(f"   → {key} > {arr[m2]} → Search RIGHT region (l = {m2+1})\n")
                l = m2 + 1
            else:
                print(f"   → {arr[m1]} < {key} < {arr[m2]} → Search MIDDLE region (l = {m1+1}, r = {m2-1})\n")
                l = m1 + 1
                r = m2 - 1

            step += 1

        return -1

    # === USER INPUT ===
    arr_input = input("Enter sorted array values separated by spaces: ")
    arr = [int(x) for x in arr_input.split()]

    key = int(input("Enter value to search: "))
    idx = ternary_search(arr, key)

    print("\n=== RESULT ===")
    if idx != -1:
        print(f"Value {key} found at index {idx}")
    else:
        print(f"Value {key} not found in array")

#SORTING ALGORITHMS

def option_seven():
    print("BUBBLE SORTING")
    print()

    # BUBBLE SORTING

    def bubble_sort(arr):
        n = len(arr)
        step = 1
        for i in range(n):
            swapped = False
            print(f"Pass {i+1}:")
            for j in range(0, n - i - 1):
                print(f"  Step {step}: Comparing index {j} ({arr[j]}) and {j+1} ({arr[j+1]})")
                step += 1
                if arr[j] > arr[j + 1]:
                    print(f"   -> Swap {arr[j]} and {arr[j+1]}")
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            print("  Current list:", arr)
            if not swapped:
                print("No swaps in this pass, list is sorted.")
                break
        return arr

    numbers_input = input("Enter numbers separated by spaces: ")
    numbers = [int(x) for x in numbers_input.split()]
    print("Original list:", numbers)

    sorted_list = bubble_sort(numbers)
    print("Final sorted list:", sorted_list)

def option_eight():
    print("\n=== SELECTION SORT ===\n")

    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            # Find the smallest element in the unsorted part
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            print(f"Pass {i+1}:")
            print(f"   Smallest element in this pass = {arr[min_index]} at index {min_index}")

            if min_index != i:
                print(f"   → Swap {arr[i]} and {arr[min_index]}")
                arr[i], arr[min_index] = arr[min_index], arr[i]
            else:
                print(f"   → No swap needed (already smallest at position {i})")

            print("   Current list:", arr, "\n")

        return arr

    # === USER INPUT ===
    numbers_input = input("Enter numbers separated by spaces: ")
    numbers = [int(x) for x in numbers_input.split()]
    print("Original list:", numbers, "\n")

    sorted_list = selection_sort(numbers)
    print("=== FINAL SORTED LIST ===")
    print(sorted_list)

def option_nine():
    print("\n=== INSERTION SORT ===\n")

    def insertion_sort(arr):
        n = len(arr)
        print("Initial array:", arr)
        print("First element is considered sorted.\n")

        for i in range(1, n):
            key = arr[i]
            j = i - 1

            print(f"Step {i}:")
            print(f"   Insert {key} into the sorted part of the array")

            # Shift elements greater than key to the right
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = key
            print("   Current list:", arr, "\n")

        return arr

    # === USER INPUT ===
    numbers_input = input("Enter numbers separated by spaces: ")
    numbers = [int(x) for x in numbers_input.split()]

    sorted_list = insertion_sort(numbers)

    print("=== FINAL SORTED LIST ===")
    print(sorted_list)


def option_ten():
    print("\n=== MERGE SORT ===\n")

    def merge_sort(arr, depth=0):
        # Base case
        if len(arr) <= 1:
            print(" " * depth*2 + f"Single element: {arr}")
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        print(" " * depth*2 + f"Step: Divide {arr} → Left={left}, Right={right}")

        # Recursive sort
        sorted_left = merge_sort(left, depth+1)
        sorted_right = merge_sort(right, depth+1)

        # Merge step
        merged = merge(sorted_left, sorted_right, depth)
        print(" " * depth*2 + f"Step: Merge {sorted_left} + {sorted_right} → {merged}")
        return merged

    def merge(left, right, depth):
        result = []
        i = j = 0

        print(" " * depth*2 + f"Merge process: Left={left}, Right={right}")

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                print(" " * depth*2 + f"   Take {left[i]} from Left")
                result.append(left[i])
                i += 1
            else:
                print(" " * depth*2 + f"   Take {right[j]} from Right")
                result.append(right[j])
                j += 1

        # Add remaining elements
        while i < len(left):
            print(" " * depth*2 + f"   Take {left[i]} from Left (remaining)")
            result.append(left[i])
            i += 1
        while j < len(right):
            print(" " * depth*2 + f"   Take {right[j]} from Right (remaining)")
            result.append(right[j])
            j += 1

        return result

    # === USER INPUT ===
    numbers_input = input("Enter numbers separated by spaces: ")
    numbers = [int(x) for x in numbers_input.split()]

    print("\nOriginal list:", numbers)
    sorted_list = merge_sort(numbers)

    print("\n=== FINAL SORTED LIST ===")
    print(sorted_list)


def option_eleven():
    print("\n=== QUICK SORT ===\n")

    def quick_sort(arr, depth=0, step=1):
        # Base case
        if len(arr) <= 1:
            return arr, step

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        # Show process in table-like format
        indent = " " * (depth * 2)
        print("{:<6} {:<20} {:<20} {:<20}".format("Step", "Pivot", "Left", "Right"))
        print("-" * 70)
        print("{:<6} {:<20} {:<20} {:<20}".format(step, str(pivot), str(left), str(right)))
        print()

        step += 1
        sorted_left, step = quick_sort(left, depth+1, step)
        sorted_right, step = quick_sort(right, depth+1, step)

        merged = sorted_left + middle + sorted_right
        print(indent + f"→ After sorting with pivot {pivot}: {merged}\n")
        return merged, step

    # === USER INPUT ===
    numbers_input = input("Enter numbers separated by spaces: ")
    numbers = [int(x) for x in numbers_input.split()]

    print("\nOriginal list:", numbers)
    sorted_list, _ = quick_sort(numbers)

    print("\n=== RESULT ===")
    print("Sorted list:", sorted_list)


def option_twelve():
    print("\n=== HEAP SORT (Min Heap & Max Heap) ===\n")

    def print_heap_tree(arr, n, ascending=True):
        """Print heap as a tree level by level with property notes."""
        level = 0
        next_level = 1
        count = 0
        print("Heap structure:")
        for i in range(n):
            print(arr[i], end="  ")
            count += 1
            if count == next_level:
                print()  # new line for next level
                level += 1
                next_level = 2 ** level
                count = 0
        print()
        if ascending:
            print("   (Max Heap property: parent ≥ children)\n")
        else:
            print("   (Min Heap property: parent ≤ children)\n")

    def heapify(arr, n, i, ascending=True):
        extreme = i
        left = 2 * i + 1
        right = 2 * i + 2

        if ascending:  # Max Heap
            if left < n and arr[left] > arr[extreme]:
                extreme = left
            if right < n and arr[right] > arr[extreme]:
                extreme = right
        else:  # Min Heap
            if left < n and arr[left] < arr[extreme]:
                extreme = left
            if right < n and arr[right] < arr[extreme]:
                extreme = right

        if extreme != i:
            print(f"   -> Swap {arr[i]} and {arr[extreme]}")
            arr[i], arr[extreme] = arr[extreme], arr[i]
            heapify(arr, n, extreme, ascending)

    def heap_sort(arr, ascending=True):
        n = len(arr)

        print("Step 1: Build {} heap...".format("Max Heap (for ascending sort)" if ascending else "Min Heap (for descending sort)"))
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i, ascending)
        print_heap_tree(arr, n, ascending)

        print("Step 2: Extract elements one by one...\n")
        for i in range(n - 1, 0, -1):
            print(f"   Extract root {arr[0]} and swap with {arr[i]}")
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0, ascending)
            print_heap_tree(arr, i, ascending)
            print(f"   Sorted portion: {arr[i:]}\n")

        return arr

    # === USER INPUT ===
    numbers_input = input("Enter numbers separated by spaces: ")
    numbers = [int(x) for x in numbers_input.split()]
    print("Original list:", numbers, "\n")

    choice = input("Sort ascending or descending? (asc/desc): ").strip().lower()
    ascending = (choice == "asc")

    sorted_list = heap_sort(numbers, ascending)

    print("\n=== FINAL SORTED LIST ===")
    print(sorted_list)

     #GREEDY ALGORITHMS

def option_thirteen():
    print("\n=== FRACTIONAL KNAPSACK ===\n")

    def fractional_knapsack(weights, values, capacity):
        items = []
        for i in range(len(weights)):
            ratio = values[i] / weights[i]
            items.append((ratio, weights[i], values[i], i+1))  # include item number

        # Sort items by value/weight ratio (descending)
        items.sort(reverse=True, key=lambda x: x[0])

        total_value = 0.0
        solution = []  # store decisions
        step = 1

        # Header
        print("{:<6} {:<8} {:<8} {:<8} {:<12}".format("Step", "Weight", "Value", "Ratio", "Decision"))
        print("-" * 55)
        print(f"Knapsack capacity: {capacity}\n")

        for ratio, weight, value, item_no in items:
            if capacity >= weight:
                capacity -= weight
                total_value += value
                decision = f"Take FULL (Item {item_no})"
                solution.append((item_no, weight, value, 1.0))
            else:
                fraction = capacity / weight
                total_value += value * fraction
                decision = f"Take {fraction*100:.1f}% (Item {item_no})"
                solution.append((item_no, weight, value, fraction))
                capacity = 0
                print("{:<6} {:<8} {:<8} {:<8.2f} {:<12}".format(step, weight, value, ratio, decision))
                break

            print("{:<6} {:<8} {:<8} {:<8.2f} {:<12}".format(step, weight, value, ratio, decision))
            step += 1

        # Show solution summary
        print("\n=== SOLUTION ===")
        for item_no, weight, value, fraction in solution:
            if fraction == 1.0:
                print(f"Item {item_no}: FULL (w={weight}, v={value})")
            else:
                print(f"Item {item_no}: {fraction*100:.1f}% (w={weight}, v={value}) → value gained = {value*fraction:.2f}")

        print(f"\nResult: Maximum value in knapsack = {total_value:.2f}")
        return total_value

    # === USER INPUT ===
    weights_input = input("Enter item weights separated by spaces: ")
    values_input = input("Enter item profits separated by spaces: ")
    weights = [int(x) for x in weights_input.split()]
    values = [int(x) for x in values_input.split()]

    capacity = int(input("Enter knapsack capacity: "))

    max_value = fractional_knapsack(weights, values, capacity)

    print("\n=== FINAL OUTPUT ===")
    print(f"Maximum value in knapsack = {max_value:.2f}")

def option_fourteen():
    print("\n=== ACTIVITY SELECTION ===\n")

    def activity_selection(start, finish):
        n = len(finish)
        activities = sorted(zip(start, finish), key=lambda x: x[1]) 

        print("{:<6} {:<10} {:<10} {:<12}".format("Step", "Start", "Finish", "Decision"))
        print("-" * 40)

        selected = []
        last_finish = -1
        step = 1

        for s, f in activities:
            if s >= last_finish:
                selected.append((s, f))
                decision = "Select"
                last_finish = f
            else:
                decision = "Skip (overlap)"

            print("{:<6} {:<10} {:<10} {:<12}".format(step, s, f, decision))
            step += 1

        # Graphing style output
        print("\n=== GRAPHING STYLE TIMELINE ===")
        max_time = max(finish)
        timeline = ["-" for _ in range(max_time+1)]

        for idx, (s, f) in enumerate(activities, start=1):
            marker = "#" if (s, f) in selected else "x"
            for t in range(s, f+1):
                timeline[t] = marker
            print(f"Activity {idx}: Start={s}, Finish={f}, {'Selected' if (s,f) in selected else 'Skipped'}")

        # Print timeline
        print("\nTimeline (Selected=#, Skipped=x):")
        print("".join(timeline))

        print("\n=== SOLUTION ===")
        for idx, (s, f) in enumerate(selected, start=1):
            print(f"Activity {idx}: Start={s}, Finish={f}")
        print(f"\nResult: Maximum set of non-overlapping activities = {len(selected)}")

        return selected

    # === USER INPUT ===
    start_input = input("Enter start times separated by spaces: ")
    finish_input = input("Enter finish times separated by spaces: ")
    start = [int(x) for x in start_input.split()]
    finish = [int(x) for x in finish_input.split()]

    selected = activity_selection(start, finish)

    print("\n=== FINAL OUTPUT ===")
    print("Selected activities:", selected)

def option_fifteen():
    print("\n=== EGYPTIAN FRACTION ===\n")

    def egyptian_fraction(numerator, denominator):
        result = []
        step = 1

        print(f"Representing {numerator}/{denominator} as Egyptian Fraction:\n")
        print("{:<6} {:<12} {:<12} {:<12} {:<20}".format("Step", "Numerator", "Denominator", "Chosen Term", "Updated Fraction"))
        print("-" * 70)

        while numerator != 0:
            # Ceiling division for next unit fraction
            x = -(-denominator // numerator)  
            result.append(x)

            # Show step details
            new_num = numerator * x - denominator
            new_den = denominator * x
            print("{:<6} {:<12} {:<12} {:<12} {:<20}".format(
                step, numerator, denominator, f"1/{x}", f"{new_num}/{new_den}"
            ))

            # Update fraction
            numerator, denominator = new_num, new_den
            step += 1

        # Show solution summary
        print("\n=== SOLUTION ===")
        print("Egyptian Fraction representation:")
        print(" + ".join([f"1/{x}" for x in result]))
        return result

    # === USER INPUT ===
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    fractions = egyptian_fraction(numerator, denominator)

    print("\n=== FINAL OUTPUT ===")
    print("Egyptian Fraction representation:", " + ".join([f"1/{x}" for x in fractions]))

import itertools

import itertools

def option_sixteen():
    print("\n=== TRAVELING SALESMAN (All Tours with Computations) ===\n")

    def tsp_all_tours(distances):
        n = len(distances)
        labels = [chr(65+i) for i in range(n)]  # A, B, C, D...

        # --- Print Guide Table ---
        print("\n=== CONFIRMATION: DISTANCE MATRIX ===")
        header = "     " + "  ".join([f"{lbl}" for lbl in labels])
        print(header)
        print("-" * (len(header)+5))
        for i in range(n):
            row = f"{labels[i]} | "
            for j in range(n):
                row += f"{distances[i][j]:5.2f}  "
            print(row)
        print()

        print("\n=== ALL POSSIBLE TOURS ===")
        start = 0  # always start at city A
        cities = list(range(n))
        others = [c for c in cities if c != start]

        results = []

        for perm in itertools.permutations(others):
            path = [start] + list(perm) + [start]
            path_letters = [labels[i] for i in path]

            # compute distances
            edge_distances = []
            total = 0
            for i in range(len(path)-1):
                frm, to = path[i], path[i+1]
                d = distances[frm][to]
                edge_distances.append(d)
                total += d

            # print tour
            print(" > ".join(path_letters), "=", "+".join(str(d) for d in edge_distances), f"= {total}")

            results.append((path_letters, edge_distances, total))

        # --- Find min and max ---
        min_total = min(r[2] for r in results)
        max_total = max(r[2] for r in results)

        min_tours = [r for r in results if r[2] == min_total]
        max_tours = [r for r in results if r[2] == max_total]

        print("\n=== SUMMARY ===")
        print(f"Minimum total distance = {min_total}")
        for path_letters, edge_distances, total in min_tours:
            print(" > ".join(path_letters), "=", "+".join(str(d) for d in edge_distances), f"= {total}")

        print(f"\nMaximum total distance = {max_total}")
        for path_letters, edge_distances, total in max_tours:
            print(" > ".join(path_letters), "=", "+".join(str(d) for d in edge_distances), f"= {total}")

    # === USER INPUT ===
    n = int(input("Enter number of cities (rows/columns): "))
    print(f"\nYou must enter {n} rows, each with {n} values (distances).")
    print("Example for 4 cities (A, B, C, D):")
    print("Row 1: 0 10 15 20")
    print("Row 2: 10 0 35 25")
    print("Row 3: 15 35 0 30")
    print("Row 4: 20 25 30 0\n")

    distances = []
    for i in range(n):
        row = list(map(int, input(f"Row {i+1} ({chr(65+i)}): ").split()))
        if len(row) != n:
            print("Error: Each row must have", n, "values.")
            return
        distances.append(row)

    tsp_all_tours(distances)

def option_seventeen():
    print("\n=== JOB SEQUENCING ===\n")

    def job_sequencing(jobs, deadlines, profits):
        # Combine job info into a list of tuples
        job_list = list(zip(jobs, deadlines, profits))
        # Sort jobs by profit (descending)
        job_list.sort(key=lambda x: x[2], reverse=True)

        print("Jobs sorted by profit (Job, Deadline, Profit):")
        for job, deadline, profit in job_list:
            print(f"{job}  Deadline={deadline}  Profit={profit}")
        print()

        n = max(deadlines)  
        slots = [-1] * n    
        total_profit = 0

        print("{:<6} {:<10} {:<10} {:<10} {:<20}".format("Step", "Job", "Deadline", "Profit", "Decision"))
        print("-" * 60)

        step = 1
        for job, deadline, profit in job_list:
            for j in range(min(n, deadline)-1, -1, -1):
                if slots[j] == -1:
                    slots[j] = job
                    total_profit += profit
                    decision = f"Scheduled at slot {j+1}"
                    break
            else:
                decision = "Skipped (no slot)"

            print("{:<6} {:<10} {:<10} {:<10} {:<20}".format(step, job, deadline, profit, decision))
            step += 1

        # Solution summary
        print("\n=== SOLUTION ===")
        for i in range(n):
            if slots[i] != -1:
                print(f"Slot {i+1}: Job {slots[i]}")
            else:
                print(f"Slot {i+1}: Empty")
        print(f"\nTotal Profit = {total_profit}")

        return slots, total_profit

    # === USER INPUT ===
    jobs_input = input("Enter job names separated by spaces: ")
    deadlines_input = input("Enter deadlines separated by spaces: ")
    profits_input = input("Enter profits separated by spaces: ")

    jobs = jobs_input.split()
    deadlines = [int(x) for x in deadlines_input.split()]
    profits = [int(x) for x in profits_input.split()]

    slots, total_profit = job_sequencing(jobs, deadlines, profits)

    print("\n=== FINAL OUTPUT ===")
    print("Scheduled jobs:", [job for job in slots if job != -1])
    print("Total profit:", total_profit)

def option_eighteen():
    print("\n=== HUFFMAN CODING (Step-by-Step, Characters + Frequencies Input) ===\n")

    import heapq

    class Node:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.freq < other.freq

    def build_huffman_tree(char_freq):
        heap = [Node(char, freq) for char, freq in char_freq.items()]
        heapq.heapify(heap)

        step = 1
        print("{:<6} {:<20} {:<20}".format("Step", "Action", "Resulting Frequency"))
        print("-" * 55)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(heap, merged)

            print("{:<6} {:<20} {:<20}".format(
                step,
                f"Merge {left.freq} + {right.freq}",
                merged.freq
            ))
            step += 1

        return heap[0]

    def generate_codes(node, prefix="", code_map={}):
        if node is None:
            return
        if node.char is not None:
            code_map[node.char] = prefix
        generate_codes(node.left, prefix + "0", code_map)
        generate_codes(node.right, prefix + "1", code_map)
        return code_map

    def decode(encoded_text, root):
        decoded = ""
        node = root
        for bit in encoded_text:
            node = node.left if bit == "0" else node.right
            if node.char is not None:
                decoded += node.char
                node = root
        return decoded

    # === USER INPUT ===
    chars = input("Enter characters separated by spaces: ").split()
    freqs = list(map(int, input("Enter frequencies separated by spaces: ").split()))

    if len(chars) != len(freqs):
        print("Error: Number of characters and frequencies must match.")
        return

    char_freq = {chars[i]: freqs[i] for i in range(len(chars))}

    print("\n=== CHARACTER FREQUENCIES (User Input) ===")
    for char, freq in char_freq.items():
        print(f"Character: {char}  Frequency: {freq}")

    # Step 2: Build Huffman Tree
    print("\n=== BUILDING HUFFMAN TREE ===")
    root = build_huffman_tree(char_freq)

    # Step 3: Generate Huffman Codes
    codes = generate_codes(root)
    print("\n=== HUFFMAN TABLE ===")
    print("{:<10} {:<15} {:<15}".format("Character", "Frequency", "Code (bits)"))
    print("-" * 40)
    total_bits = 0
    breakdowns = []
    for char, freq in char_freq.items():
        bits = len(codes[char])
        total_bits += freq * bits
        breakdowns.append(f"{freq}×{bits}")
        print("{:<10} {:<15} {:<15}".format(char, freq, f"{codes[char]} ({bits})"))

    # Step 4: Encode a message
    message = input("\nEnter a message using these characters: ")
    encoded_text = "".join(codes[char] for char in message)
    print("\n=== ENCODING PROCESS (Step-by-Step) ===")
    for i, char in enumerate(message, start=1):
        print(f"Step {i}: {char} -> {codes[char]}")
    print("Encoded message:", encoded_text)
    print(f"Message length: {len(encoded_text)} bits")

    # Step 5: Decode text
    decoded_text = decode(encoded_text, root)
    print("\n=== DECODING PROCESS ===")
    print("Decoded text:", decoded_text)

    # Step 6: Final Compression Summary (PPT style)
    original_bits = len(message) * 8  # ASCII size
    print("\n=== SUMMARY ===")
    print(f"original ASCII: {original_bits} bits ({len(message)}×8)")
    print(f"message: {len(encoded_text)} bits")
    print(f"tree/table: {total_bits} bits ({' + '.join(breakdowns)})")
    print(f"totalofBits: {len(encoded_text) + total_bits} bits ({len(encoded_text)} + {total_bits})")


# GRAPH ALGORITHMS

def option_nineteen():
    print("\n=== KRUSKAL'S ALGORITHM ===\n")

    class DisjointSet:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n

        def find(self, u):
            if self.parent[u] != u:
                self.parent[u] = self.find(self.parent[u])
            return self.parent[u]

        def union(self, u, v):
            root_u = self.find(u)
            root_v = self.find(v)
            if root_u != root_v:
                if self.rank[root_u] < self.rank[root_v]:
                    self.parent[root_u] = root_v
                elif self.rank[root_u] > self.rank[root_v]:
                    self.parent[root_v] = root_u
                else:
                    self.parent[root_v] = root_u
                    self.rank[root_u] += 1
                return True
            return False

    def kruskal(n, edges, labels):
        edges.sort(key=lambda x: x[2])
        ds = DisjointSet(n)
        mst = []
        total_weight = 0

        print("{:<6} {:<12} {:<12} {:<12}".format("Step", "Edge", "Weight", "Decision"))
        print("-" * 45)

        step = 1
        for u, v, w in edges:
            if ds.union(u, v):
                mst.append((u, v, w))
                total_weight += w
                decision = "Include"
            else:
                decision = "Skip (cycle)"
            print("{:<6} {:<12} {:<12} {:<12}".format(step, f"{labels[u]}-{labels[v]}", w, decision))
            step += 1

        return mst, total_weight

    n = int(input("Enter number of vertices: "))
    labels = [chr(65+i) for i in range(n)]
    m = int(input("Enter number of edges: "))
    edges = []
    print("\nEnter edges as: Vertex1 Vertex2 Weight")
    for _ in range(m):
        u, v, w = input().split()
        edges.append((labels.index(u), labels.index(v), int(w)))

    mst, total_weight = kruskal(n, edges, labels)

    print("\n=== MINIMUM SPANNING TREE ===")
    for u, v, w in mst:
        print(f"{labels[u]} - {labels[v]} : {w}")
    print(f"Total weight of MST: {total_weight}")


def option_twenty():
    print("\n=== BORUVKA'S ALGORITHM ===\n")

    class DisjointSet:
        def __init__(self, n):
            self.parent = list(range(n))

        def find(self, u):
            if self.parent[u] != u:
                self.parent[u] = self.find(self.parent[u])
            return self.parent[u]

        def union(self, u, v):
            root_u = self.find(u)
            root_v = self.find(v)
            if root_u != root_v:
                self.parent[root_v] = root_u
                return True
            return False

    def boruvka(n, edges, labels):
        ds = DisjointSet(n)
        mst = []
        total_weight = 0
        num_components = n
        round_num = 1

        while num_components > 1:
            cheapest = [-1] * n
            print(f"\n=== ROUND {round_num} ===")
            print("{:<6} {:<12} {:<12} {:<12}".format("Step", "Component", "Chosen Edge", "Weight"))
            print("-" * 45)

            step = 1
            for idx, (u, v, w) in enumerate(edges):
                set_u = ds.find(u)
                set_v = ds.find(v)
                if set_u != set_v:
                    if cheapest[set_u] == -1 or edges[cheapest[set_u]][2] > w:
                        cheapest[set_u] = idx
                    if cheapest[set_v] == -1 or edges[cheapest[set_v]][2] > w:
                        cheapest[set_v] = idx

            for i in range(n):
                if cheapest[i] != -1:
                    u, v, w = edges[cheapest[i]]
                    if ds.union(u, v):
                        mst.append((u, v, w))
                        total_weight += w
                        num_components -= 1
                        print("{:<6} {:<12} {:<12} {:<12}".format(step, f"Comp {i}", f"{labels[u]}-{labels[v]}", w))
                        step += 1

            round_num += 1

        return mst, total_weight

    n = int(input("Enter number of vertices: "))
    labels = [chr(65+i) for i in range(n)]
    m = int(input("Enter number of edges: "))
    edges = []
    print("\nEnter edges as: Vertex1 Vertex2 Weight")
    for _ in range(m):
        u, v, w = input().split()
        edges.append((labels.index(u), labels.index(v), int(w)))

    mst, total_weight = boruvka(n, edges, labels)

    print("\n=== MINIMUM SPANNING TREE ===")
    for u, v, w in mst:
        print(f"{labels[u]} - {labels[v]} : {w}")
    print(f"Total weight of MST: {total_weight}")

def option_twentyOne():
    print("\n=== PRIM'S ALGORITHM ===\n")

    import heapq

    def prim(n, edges, labels):
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))

        visited = [False] * n
        mst = []
        total_weight = 0
        min_heap = [(0, 0, -1)]
        step = 1

        print("{:<6} {:<10} {:<10} {:<10} {:<15}".format("Step", "From", "To", "Weight", "Total"))
        print("-" * 55)

        while min_heap:
            w, u, parent = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            if parent != -1:
                mst.append((parent, u, w))
                total_weight += w
                print("{:<6} {:<10} {:<10} {:<10} {:<15}".format(step, labels[parent], labels[u], w, total_weight))
                step += 1

            for edge in graph[u]:
                if not visited[edge[1]]:
                    heapq.heappush(min_heap, (edge[0], edge[1], u))

        return mst, total_weight

    n = int(input("Enter number of vertices: "))
    labels = [chr(65+i) for i in range(n)]
    m = int(input("Enter number of edges: "))
    edges = []
    print("\nEnter edges as: Vertex1 Vertex2 Weight")
    for _ in range(m):
        u, v, w = input().split()
        edges.append((labels.index(u), labels.index(v), int(w)))

    mst, total_weight = prim(n, edges, labels)

    print("\n=== MINIMUM SPANNING TREE ===")
    for u, v, w in mst:
        print(f"{labels[u]} - {labels[v]} : {w}")
    print(f"Total weight of MST: {total_weight}")


def option_twentyTwo():
    print("\n=== DIAL'S ALGORITHM (Enhanced) ===\n")

    from collections import deque

    def dial_algorithm(graph, src, max_weight, labels, target):
        n = len(graph)
        dist = [float("inf")] * n
        parent = [-1] * n  # track shortest path tree
        dist[src] = 0
        buckets = [deque() for _ in range(max_weight * n + 1)]
        buckets[0].append(src)
        idx = 0
        step = 1

        print("{:<6} {:<12} {:<12} {:<12} {:<12}".format("Step", "Selected", "Neighbor", "Old Dist", "New Dist"))
        print("-" * 65)

        while True:
            while idx < len(buckets) and not buckets[idx]:
                idx += 1
            if idx == len(buckets):
                break

            u = buckets[idx].popleft()
            # show selected vertex
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    old_dist = dist[v]
                    dist[v] = dist[u] + w
                    parent[v] = u
                    buckets[dist[v]].append(v)
                    print("{:<6} {:<12} {:<12} {:<12} {:<12}".format(
                        step, labels[u], labels[v], old_dist, dist[v]
                    ))
                    step += 1

        # --- Shortest Path Reconstruction ---
        path = []
        cur = target
        while cur != -1:
            path.append(labels[cur])
            cur = parent[cur]
        path.reverse()

        return dist, path

    # === USER INPUT ===
    n = int(input("Enter number of vertices: "))
    labels = []
    print("Enter vertex labels one by one:")
    for i in range(n):
        labels.append(input(f"Label for vertex {i+1}: "))

    m = int(input("Enter number of edges: "))
    graph = [[] for _ in range(n)]
    max_weight = 0

    print("\nEnter edges as: Vertex1 Vertex2 Weight")
    for _ in range(m):
        u, v, w = input().split()
        u_index = labels.index(u)
        v_index = labels.index(v)
        graph[u_index].append((v_index, int(w)))
        graph[v_index].append((u_index, int(w)))
        max_weight = max(max_weight, int(w))

    src_label = input("Enter source vertex: ")
    src = labels.index(src_label)
    target_label = input("Enter target vertex: ")
    target = labels.index(target_label)

    dist, path = dial_algorithm(graph, src, max_weight, labels, target)

    print("\n=== FINAL DISTANCES FROM SOURCE", src_label, "===")
    print("{:<10} {:<15}".format("Vertex", "Distance"))
    print("-" * 30)
    for i in range(n):
        print("{:<10} {:<15}".format(labels[i], dist[i]))

    print("\n=== SHORTEST PATH ===")
    print(f"{src_label} → {target_label} : {' > '.join(path)}")
    print(f"Total cost: {dist[target]}")

def option_twentyThree():
    print("\n=== DIJKSTRA'S ALGORITHM (Enhanced Step-by-Step) ===\n")

    import heapq

    def dijkstra(n, graph, src, labels, target):
        dist = [float("inf")] * n
        parent = [-1] * n
        dist[src] = 0
        pq = [(0, src)]  # (distance, vertex)
        step = 1

        print("{:<6} {:<12} {:<12} {:<12} {:<15}".format(
            "Step", "Action", "Vertex", "Old Dist", "New Dist"))
        print("-" * 65)

        while pq:
            d, u = heapq.heappop(pq)
            print("{:<6} {:<12} {:<12} {:<12} {:<15}".format(
                step, "Heap Pop", labels[u], dist[u], dist[u]))
            step += 1

            if d > dist[u]:
                continue

            for v, w in graph[u]:
                print("{:<6} {:<12} {:<12} {:<12} {:<15}".format(
                    step, "Check Edge", f"{labels[u]}-{labels[v]}",
                    dist[v], dist[u] + w))
                step += 1

                if dist[v] > dist[u] + w:
                    old_dist = dist[v]
                    dist[v] = dist[u] + w
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v))
                    print("{:<6} {:<12} {:<12} {:<12} {:<15}".format(
                        step, "Update", labels[v], old_dist, dist[v]))
                    step += 1

        # --- Shortest Path Reconstruction ---
        path = []
        cur = target
        while cur != -1:
            path.append(labels[cur])
            cur = parent[cur]
        path.reverse()

        return dist, path

    # === USER INPUT ===
    n = int(input("Enter number of vertices: "))
    labels = []
    print("Enter vertex labels one by one:")
    for i in range(n):
        labels.append(input(f"Label for vertex {i+1}: "))

    m = int(input("Enter number of edges: "))
    graph = [[] for _ in range(n)]
    max_weight = 0

    print("\nEnter edges as: Vertex1 Vertex2 Weight (non-negative integer)")
    for _ in range(m):
        u, v, w = input().split()
        u_index = labels.index(u)
        v_index = labels.index(v)
        w = int(w)
        graph[u_index].append((v_index, w))
        graph[v_index].append((u_index, w))  # undirected
        max_weight = max(max_weight, w)

    src_label = labels[0]   # first vertex
    src = 0
    target_label = labels[-1]  # last vertex
    target = n - 1

    dist, path = dijkstra(n, graph, src, labels, target)

    print("\n=== FINAL DISTANCES FROM SOURCE", src_label, "===")
    print("{:<10} {:<15}".format("Vertex", "Distance"))
    print("-" * 30)
    for i in range(n):
        print("{:<10} {:<15}".format(labels[i], dist[i]))

    print("\n=== SUMMARY ===")
    print("Maximum edge weight:", max_weight)
    print("Shortest path from", src_label, "to", target_label, ":", " > ".join(path))
    print("Total shortest path cost:", dist[target])

def searching_menu():
    while True:

        print("")
        print("SEARCHING ALGORITHMS")
        print("1 Linear Search")
        print("2 Binary Search")
        print("3 Interpolation Search")
        print("4 Jump Search")
        print("5 Exponential Search")
        print("6 Ternary Search")
        print("0 Back")

        c=input("Select: ")

        if c=="1": option_one()
        elif c=="2": option_two()
        elif c=="3": option_three()
        elif c=="4": option_four()
        elif c=="5": option_five()
        elif c=="6": option_six()
        elif c=="0": break


def sorting_menu():
    while True:

        print("")
        print("SORTING ALGORITHMS")
        print("7 Bubble Sort")
        print("8 Selection Sort")
        print("9 Insertion Sort")
        print("10 Merge Sort")
        print("11 Quick Sort")
        print("12 Heap Sort")
        print("0 Back")

        c=input("Select: ")

        if c=="7": option_seven()
        elif c=="8": option_eight()
        elif c=="9": option_nine()
        elif c=="10": option_ten()
        elif c=="11": option_eleven()
        elif c=="12": option_twelve()
        elif c=="0": break


def greedy_menu():

    while True:

        print("")   
        print("GREEDY ALGORITHMS")
        print("13 Fractional Knapsack")
        print("14 Activity Selection")
        print("15 Egyptian Fraction")
        print("16 Traveling Salesman")
        print("17 Job Sequencing")
        print("18 Huffman Coding")
        print("0 Back")

        c=input("Select: ")

        if c=="13": option_thirteen()
        elif c=="14": option_fourteen()
        elif c=="15": option_fifteen()
        elif c=="16": option_sixteen()
        elif c=="17": option_seventeen()
        elif c=="18": option_eighteen()
        elif c=="0": break

def graph_menu():

    while True:

        print("")   
        print("GRAPH ALGORITHMS")
        print("19 Kruskal's")
        print("20 Boruvka's")
        print("21 Prim's")
        print("22 Dial's")
        print("23 Dijkstra's")
        print("0 Back")

        c=input("Select: ")

        if c=="19": option_nineteen()
        elif c=="20": option_twenty()
        elif c=="21": option_twentyOne()
        elif c=="22": option_twentyTwo()
        elif c=="23": option_twentyThree()
        elif c=="0": break

def main_menu():

    while True:

        print("")
        print(">--------------------<")
        print("      MAIN MENU")
        print(">--------------------<")

        print("1 Searching Algorithms")
        print("2 Sorting Algorithms")
        print("3 Greedy Algorithms")
        print("4 Graph Algorithms")
        print("0 Exit")

        choice=input("Select: ")

        if choice=="1":
            searching_menu()

        elif choice=="2":
            sorting_menu()

        elif choice=="3":
            greedy_menu()

        elif choice=="4":
            graph_menu()

        elif choice=="0":
            print("Program terminated")
            break
main_menu()
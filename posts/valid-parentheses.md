---
title: Valid parentheses problem
description: How I solved valid parentheses using less memory
tags:
  - exercise
  - algorithm
  - memory
  - go
  - performance
  - optimization
  - bit manipulation
date: 27-08-2025
---

[The valid parentheses problem](https://leetcode.com/problems/valid-parentheses/) is an easy
problem to solve. The algorithm is:

```
stack = []
for every char in str
  if char is an opening parenthesis
    stack.push (char)

  if char is a closing parenthesis
    if stack is empty
      error ()

    top = stack.pop ()
    if char does not match top
      error ()

if stack is not empty
  error ()

success ()
```

When I thought of ways to reduce the memory usage of this algorithm, bit-packing came to my mind.

Using a `rune` (32-bit integer) for each parenthesis seemed wasteful. So, I
decided to use an 8-bit integer, but the problem was, I'd need to use at least
7 bits to represent a parenthesis, because the biggest ASCII code-point I needed
to store was 123, and it required 7 bits (`01111011`). Then I quickly realized I
didn't need to use ASCII. I can encode them however I want. I gave each kind of parenthesis a number:
1 for round, 2 for braces, and 3 for square brackets

The next task was to fit multiple parens inside an integer. I chose `[]uint8` as the stack.
Since each paren used only 2 bits, I could fit 4 parens inside an 8 bit number. When a number
was used up, I pushed a new number.

In the end, I successfully wrote the program.

Here's the Go code followed by a brief explanation.

```go
func isValid(s string) bool {
	const (
		paren  uint8 = 1
		curly  uint8 = 2
		square uint8 = 3
	)

	stack := []uint8{0}
	shift := 0

	for _, c := range s {
		if shift == 8 {
			stack = append(stack, 0)
			shift = 0
		}

		var kind uint8

		switch c {
		case '(', ')':
			kind = paren
		case '{', '}':
			kind = curly
		case '[', ']':
			kind = square
		}

		switch c {
		case '(', '{', '[':
			stack[len(stack)-1] |= (kind << shift)
			shift += 2

		default:
			shift -= 2

			if shift < 0 {
				if len(stack) > 1 {
					stack = stack[:len(stack)-1]
				}
				shift = 6
			}

			top := stack[len(stack)-1]

			if (top>>shift)&kind != kind {
				return false
			}
		}
	}

	return len(stack) == 1 && shift == 0
}
```

The `shift` variable is important. It keeps track of the next bit position in the "top" number.

When the program encounters an opening paren, it places the 2-bit representation of the paren where
`shift` points to. It does this by combining two bit patterns using the bitwise OR operator (`|`).
In the `default` case, `shift` is immediately reduced by 2. This is equivalent to `top = stack.pop ()`.
Then the program checks whether the top number is still needed or can be discarded.

The `shift` variable is set to `6` if we pop the stack. This ensures the next bit-pattern is placed
in the most significant 2 bits of the number. To check whether the parens match, we perform a mask on
the number. The mask is the opening paren we are looking for.

If the loop terminates without errors, then we check if we have matched all opening parens with their lovers
by checking that the stack contains a single number and that `shift` is 0.


### Notes

* I used to zero-out the opening paren's bit-pattern when it was matched using this line of code:
`stack[len(stack)-1] &^= kind << shift`. It was redundant. Just overwrite the number. `shift` is guiding you anyways.

* The solution beats `98.52%` (using 3.95 MB) of solutions in memory consumption. Not always; sometimes it
uses 4.14 MB, which beats `63.49%` of solutions. The difference is small, but the change in percentage
is big.

---

Experienced programmers might see a lot of other opportunities for improvement or even
different ways of solving this problem.

It was a fun bit-packing exercise.

Have a nice day.


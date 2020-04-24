// https://leetcode.com/problems/happy-number/submissions/

func isHappy(n int) bool {
    numbersSeen := make(map[int]bool)

    for {
        n = processNumber(n)
        // this number is repeating infinitely
        if numbersSeen[n] == true {
            return false
        }
        // happy number yay!
        if n == 1 {
            return true
        }
        numbersSeen[n] = true
    }
    
    // this point should never be reached
    return false
}

func processNumber(number int) (sum int) {
    maxDigits := getMaxDigits(number)
    
    // fmt.Printf("max digits for %d is %d \n", number, maxDigits)

    for digit := 0; digit < maxDigits; digit++ {
        thisDigit := getDigit(number, digit)
        
        // fmt.Printf("the digit %d for %d is %d \n", digit, number, thisDigit)
        
        sum += int(
            math.Pow(
                float64(thisDigit),
                float64(2),
            ),
        )    
	}    

    // fmt.Printf("sum was %d \n", sum)
    
    return sum
}

func getMaxDigits(number int) (maxDigits int) {
    for {
        // I ran into a bug here, where `>` had to be switched
        // to `>=`, to account for cases like `100`
        if number >= int(math.Pow10(maxDigits)) {
            maxDigits += 1
        } else {
            return maxDigits
        }
    }
    
    return maxDigits    
}

func getDigit(number int, digit int) (result int) {
    // leading digit clip
    result = number % int(math.Pow10(digit + 1))
    
    // trailing digit clip
    result = result / int(math.Pow10(digit))
    
    return result
}

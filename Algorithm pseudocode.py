Initialize length_counter := 0
Initialize word_counter := 1         // Start at 1 because the first word starts before any space
Initialize vowel_counter := 0

Read character ch

WHILE ch != '.' DO
    length_counter := length_counter + 1
    
    IF ch == ' ' THEN
        word_counter := word_counter + 1
    END_IF
    
    IF ch IN ['a','e','i','o','u','A','E','I','O','U'] THEN
        vowel_counter := vowel_counter + 1
    END_IF
    
    Read next character ch
END_WHILE

Output "Length of sentence: ", length_counter + 1    // +1 to include the period
Output "Number of words: ", word_counter
Output "Number of vowels: ", vowel_counter

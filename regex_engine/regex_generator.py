import re

class generator:
    def __compute_numerical_range(
        self, str_a, str_b, any_digit="[0-9]", start_appender_str=""
    ):
        """
        Helps generating regex for numerical range.
        Assumptions are int(str_a) <= int(str_b) and should have equal number of digits.
        """
        str_len = len(str_a)
        if len(str_a) != len(str_b):
            raise (
                Exception(
                    f"The input numbers ({str_a}, {str_b}) should have equal number of digits"
                )
            )

        # Three edge cases
        if str_a == str_b:
            return start_appender_str+str_a
        if str_len == 1:
            return f"{start_appender_str}[{str_a}-{str_b}]"
        # Counting index position till the characteres are equal
        check_equal = -1
        for i in range(str_len):
            if str_a[i] == str_b[i]:
                check_equal += 1
            else:
                break
        if check_equal != -1:
            return self.__compute_numerical_range(
                str_a[check_equal + 1 :],
                str_b[check_equal + 1 :],
                any_digit=any_digit,
                start_appender_str=start_appender_str + str_a[: check_equal + 1],
            )

        # Example 1: 169 - 543
        # Intermediate range
        intermediate_range = list(range(int(str_a[0]) + 1, int(str_b[0])))
        patterns = []
        if intermediate_range:
            patterns.append(
                f"{start_appender_str}[{intermediate_range[0]}-{intermediate_range[-1]}]{''.join([any_digit]*(str_len-1))}"
            )
        # patterns for the above part ['[2-4][0-9][0-9]']

        # Case for str_a
        for loop_counter in range(str_len - 1):  # no_of_digits-1 units
            if loop_counter == str_len - 2:  # Find the last loop
                patterns.append(
                    f"{start_appender_str}{str_a[:loop_counter+1]}[{str_a[-1]}-9]"
                )
            else:
                if str_a[loop_counter+1] != '9':  # if 599 then avoid 10 in '[6-8]...|5[10-9]..|59[9-9].|598[9-9]'
                    patterns.append(
                        f"{start_appender_str}{str_a[:loop_counter+1]}[{int(str_a[loop_counter+1])+1}-9]{''.join([any_digit]*(str_len-2-loop_counter))}"
                    )
        # patterns for the above part ['1[7-9][0-9]','16[9-9]']

        # Case for str_b
        for loop_counter in range(str_len - 1):  # no_of_digits-1 units
            if loop_counter == str_len - 2:  # Find the last loop
                patterns.append(
                    f"{start_appender_str}{str_b[:loop_counter+1]}[0-{str_b[-1]}]"
                )
            else:
                if str_b[loop_counter+1] != '0':  # if 1102 then avoid -1 in '11[0--1].|110[0-2]'
                    patterns.append(
                        f"{start_appender_str}{str_b[:loop_counter+1]}[0-{int(str_b[loop_counter+1])-1}]{''.join([any_digit]*(str_len-2-loop_counter))}"
                    )
        # patterns for the above part ['5[0-3][0-9]','54[0-3]']

        return "|".join(patterns)

    def __range_splitter(self, a, b):
        """
        Given two numbers, split them into multiple range.
        Such that each range has equal number of digits.

        Example:
            range : -15 and 256
            output : [(1, 9, '-'), 
                      (10, 15, '-'),
                      (0, 9, ''),
                      (10, 99, ''),
                      (100, 256, '')]

            The third element denotes the sign.
            ie, Positive('') or Negative('-').

        Output Type : List
        Assumption : a <= b.
        """
        ranges = []
        # Entire range negative
        if b <= 0:  # a <= 0 implicit
            sign = "-"
            a, b = abs(a), abs(b)
            a, b = (a, b) if a < b else (b, a)
        # Entire range positive
        elif a >= 0:  # b >= 0 implicit
            sign = ""
        # Range between negative and positive
        else:
            ranges.extend(self.__range_splitter(a, -1))
            ranges.extend(self.__range_splitter(0, b))
            return ranges

        str_a = str(a)
        str_b = str(b)
        len_str_a = len(str_a)
        len_str_b = len(str_b)

        if len_str_a == len_str_b:
            ranges.append((a, b, sign))
        else:
            for loop_counter in range(len_str_a, len_str_b + 1):
                if loop_counter == len_str_a:
                    ranges.append((a, int("".join(["9"] * loop_counter)), sign))
                elif loop_counter == len_str_b:
                    ranges.append((ranges[-1][1] + 1, b, sign))
                else:
                    ranges.append(
                        (ranges[-1][1] + 1, int("".join(["9"] * loop_counter)), sign)
                    )

        return ranges


    def numerical_range(self, a, b):
        """
        Generate regex for matching a number between a range.
        The regex might not be optimal but it serves the purpose. 
        
        You get what you give.
        ie, If you pass two floating number the regex can only match floating number,
        else if you pass two integer number you can only mtach integer number.
        """
        # Handling floating point numbers
        if (isinstance(a, (float)) and isinstance(b, (float, int))) or (
            isinstance(a, (float, int)) and isinstance(b, (float))
        ):
            a, b = (a, b) if a < b else (b, a)
            num_of_decimal_in_a = len(str(float(a))) - (str(float(a)).find(".") + 1)
            num_of_decimal_in_b = len(str(float(b))) - (str(float(b)).find(".") + 1)
            max_num_decimal = max(num_of_decimal_in_a, num_of_decimal_in_b)

            # Properly removing floating point and converting to integer
            a, b = (
                "".join([c for c in str(float(a)) if c != "."]),
                "".join([c for c in str(float(b)) if c != "."]),
            )
            if len(str(a)) < len(str(b)):
                a = a + f"{'0'*(max_num_decimal-num_of_decimal_in_a)}"
            else:
                b = b + f"{'0'*(max_num_decimal-num_of_decimal_in_b)}"
            a, b = int(a), int(b)
            a, b = (a, b) if a < b else (b, a)

            # Generate regex by treating float as integer
            ranges = self.__range_splitter(a, b)
            intermediate_regex = "|".join(
                [
                    self.__compute_numerical_range(
                        str(r[0]), str(r[1]), any_digit="[0-9]", start_appender_str=r[2]
                    )
                    for r in ranges
                ]
            )

            # Modifying the integer supported regex to support float
            new_regex = []
            for p in intermediate_regex.split("|"):
                if p.find('[') == -1:
                    x = [c for c in p if c != '-']
                else:
                    x = [
                        c for d in re.findall(r"-{0,1}(\d+)\[\d-\d\]*", p) for c in d
                    ] + re.findall(r"-{0,1}[\d]*(\[\d-\d\]*)", p)

                # If x = ['[0-9]'] and max_num_decimal = 2, We need x = ['0','[0-9]']
                if len(x) < max_num_decimal:
                    x = (['0']*(max_num_decimal-len(x))) + x

                # Example x = ['3', '2', '[0-1]', '[0-9]'] for p=32[0-1][0-9]
                start_appender_str = "-" if re.findall("^-", p) else ""
                # Add a decimal point inbetween, keep the next digit mandatory and others optional (32.[0-1][0-9]?[0-9]*)
                fractional_part = (
                    [x[-max_num_decimal]] + [z + "?" for z in x[-max_num_decimal + 1 :]]
                    if max_num_decimal > 1
                    else [z for z in x[-max_num_decimal:]]
                )
                non_fractional_part = ''.join(x[:-max_num_decimal]) if ''.join(x[:-max_num_decimal]) else '0?'
                new_regex.append(
                    f"{start_appender_str}{non_fractional_part}\.{''.join(fractional_part)}[0-9]*"
                )
            regex = f"^({'|'.join(new_regex)})$"
            return regex

        # Handling integer numbers
        elif isinstance(a, (int)) and isinstance(b, (int)):
            a, b = (a, b) if a < b else (b, a)
            ranges = self.__range_splitter(a, b)
            regex = f"^({'|'.join([self.__compute_numerical_range(str(r[0]),str(r[1]),any_digit='[0-9]',start_appender_str=r[2]) for r in ranges])})$"
            return regex

        # Neither integer nor float
        else:
            raise (
                Exception(
                    f"Unsupported data types for {a}:{type(a)} or {b}:{type(a)}, Only supported float/int"
                )
            )
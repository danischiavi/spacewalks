from eva_data_analysis import text_to_duration

def test_text_to_duration():
    actual = text_to_duration("10:00")
    expected = 10.00
    assert(actual == expected)

    # if (actual == expected):
    #     print("Pass")
    # else:
    #     print("Fail")


# Convention over configuration
# pytest:
# looks for scripts that start with test_ 
# python3 -m pytest --> runs all the test_ scripts

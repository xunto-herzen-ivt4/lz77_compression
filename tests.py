import lz77

tests = [
    {
        "message": "кибернетики",
        "buffer_size": 4,
        "dict_size": 12,
        "result": [
            (0, 0, 'к'),
            (0, 0, 'и'),
            (0, 0, 'б'),
            (0, 0, 'е'),
            (0, 0, 'р'),
            (0, 0, 'н'),
            (3, 1, 'т'),
            (7, 1, 'к'),
            (2, 1, '')
        ]
    },
    {
        "message": "аааааааааааа",
        "buffer_size": 4,
        "dict_size": 12,
        "result": [
            (0, 0, 'а'),
            (1, 1, 'а'),
            (3, 3, 'а'),
            (4, 4, 'а')
        ]
    }
]

for test in tests:
    result = lz77.compress(test['message'], test['buffer_size'], test['dict_size'])
    print(result)
    assert result == test['result']

    message = lz77.decompress(test['result'])
    print(message)
    assert message == test['message']
    print('===========================')
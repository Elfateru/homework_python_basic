server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for i_key, i_val in server_data.items():
    print(i_key,':')
    for j_key, j_val in i_val.items():
        print('    ', j_key, ':', j_val)
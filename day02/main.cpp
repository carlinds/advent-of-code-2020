#include <string>
#include <vector>
#include <iostream>

struct PasswordPolicy {
    char required_char;
    int lb;
    int ub;
};

struct PasswordData {
    PasswordPolicy policy;
    std::string password;
};

std::vector<PasswordData> read_stdin() {
    std::vector<PasswordData> passwords{};

    std::string line;
    while (std::getline(std::cin, line)) {
        PasswordData pw_data{};

        int start_pos = 0;
        int end_pos = line.find("-");
        pw_data.policy.lb = std::stoi(line.substr(start_pos, end_pos));

        start_pos = end_pos + 1;
        end_pos = line.find(" ");
        pw_data.policy.ub = std::stoi(line.substr(start_pos, end_pos - start_pos));

        start_pos = end_pos + 1;
        pw_data.policy.required_char = line[start_pos];

        start_pos += 3;
        pw_data.password = line.substr(start_pos);

        passwords.push_back(pw_data);
    }

    return passwords;
}

bool first_policy(PasswordData pw_data) {
    int n_occurrences{0};
    for (char const c : pw_data.password) {
        if (c == pw_data.policy.required_char) {
            n_occurrences++;
        }
    }

    return n_occurrences >= pw_data.policy.lb && n_occurrences <= pw_data.policy.ub;
}

bool second_policy(PasswordData pw_data) {
    std::string password{pw_data.password};

    int n_matches{0};
    if (password[pw_data.policy.lb - 1] == pw_data.policy.required_char) {
        n_matches++;
    }

    if (password[pw_data.policy.ub - 1] == pw_data.policy.required_char) {
        n_matches++;
    }

    return n_matches == 1;
}

int main() {
    std::vector<PasswordData> passwords{read_stdin()};

    int first_policy_passwords{0};
    int second_policy_passwords{0};
    for (auto const pw_data : passwords) {
        if (first_policy(pw_data)) {
            first_policy_passwords++;
        }

        if (second_policy(pw_data)) {
            second_policy_passwords++;
        }
    }

    std::cout << "Valid passwords with first policy: " << first_policy_passwords << "\n";
    std::cout << "Valid passwords with second policy: " << second_policy_passwords << "\n";

    return 0;
}

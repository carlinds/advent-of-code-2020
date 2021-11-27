#include <algorithm>
#include <functional>
#include <string>
#include <iostream>
#include <vector>
#include <cstdint>

void read_stdin(std::vector<uint32_t> &buffer) {
	std::string line;
	while (std::getline(std::cin, line)) {
		buffer.push_back(std::stoi(line));	
	}
}


int get_combinations(std::vector<uint32_t> const& input,
					 int const n_combinations) {
	std::vector<bool> permutation_vector(input.size());
	std::fill(permutation_vector.end()-n_combinations, permutation_vector.end(), true);

	do {
		uint32_t sum{0};
		uint32_t result{1};

		for (int i{0}; i < input.size(); ++i) {
			if (permutation_vector[i]) {
				sum += input[i];
				result *= input[i];
			}
		}

		if (sum == 2020) {
			return result;
		}

	} while (std::next_permutation(permutation_vector.begin(), permutation_vector.end()));

	return 0;
}


int main() {

	std::vector<uint32_t> input = {};
	read_stdin(input);
	int two_entries_result{get_combinations(input, 2)};
	int three_entries_result{get_combinations(input, 3)};

	std::cout << "Two entries result: " << two_entries_result << "\n";
	std::cout << "Three entries result: " << three_entries_result << "\n";
	return 0;
}


import gopax_public
import json

def main():
	print("hello")
	gopax = gopax_public.gopax()
	test = gopax.trading_pairs()
	print(len(test))
	print(json.dumps(test, sort_keys=True, indent=4))
main()
import sys
import antigravity

def calculate_geohash():
	if len(sys.argv) != 4:
		print("Error: Invalid number of arguments.")
		print("Usage: python3 geohashing.py <latitude> <longitude> <datedow>")
		return
	try:
		latitude = float(sys.argv[1])
		longitude= float(sys.argv[2])
		datedow = sys.argv[3].encode('utf-8')
		antigravity.geohash(latitude,longitude,datedow)
	except ValueError:
		print("Error: Latitude and longitude must be valid numbers.")
	except Exception as e:
		print(f"Error: An unexpected issue occurred - {e}")

if __name__ == '__main__':
	calculate_geohash()

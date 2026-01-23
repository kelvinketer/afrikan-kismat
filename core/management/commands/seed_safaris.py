from django.core.management.base import BaseCommand
from core.models import SafariPackage, ItineraryDay

class Command(BaseCommand):
    help = 'Seeds the database with 10 high-performing safari packages'

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data (optional)...")
        # Optional: Clean slate. Comment out if you want to keep existing data.
        # SafariPackage.objects.all().delete()

        safaris = [
            {
                "title": "3-Day Masai Mara Budget Adventure",
                "price_usd": 450.00,
                "duration": "3 Days / 2 Nights",
                "location": "Masai Mara",
                "image": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1200&q=80",
                "desc": "The ultimate quick getaway to the world's most famous reserve. Perfect for budget travelers and those short on time who want to witness the Big 5.",
                "days": [
                    ("Nairobi to Masai Mara", "Depart Nairobi at 7 AM. Drive through the Great Rift Valley. Arrive for lunch and an afternoon game drive."),
                    ("Full Day Game Viewing", "Spend the entire day exploring the Mara plains. Look out for the Big 5 and the Great Migration (seasonal). Picnic lunch by the Mara River."),
                    ("Morning Drive & Return", "Early morning game drive to catch predators. Breakfast and drive back to Nairobi, arriving by 4 PM.")
                ]
            },
            {
                "title": "4-Day Lake Nakuru & Masai Mara",
                "price_usd": 850.00,
                "duration": "4 Days / 3 Nights",
                "location": "Nakuru & Mara",
                "image": "https://images.unsplash.com/photo-1534700736906-8d697b87c71e?auto=format&fit=crop&w=1200&q=80",
                "desc": "A perfect blend of bird watching, rhino tracking in Nakuru, and big cat action in the Mara.",
                "days": [
                    ("Nairobi to Lake Nakuru", "Drive to Lake Nakuru. Afternoon game drive to see Rhinos and Flamingos."),
                    ("Nakuru to Masai Mara", "Morning drive to Masai Mara. Arrive for a late afternoon game drive."),
                    ("Masai Mara Experience", "Full day game drive with picnic lunch. Optional Maasai Village visit in the evening."),
                    ("Return to Nairobi", "Sunrise game drive, breakfast, and return journey to Nairobi.")
                ]
            },
            {
                "title": "3-Day Amboseli Elephant Safari",
                "price_usd": 520.00,
                "duration": "3 Days / 2 Nights",
                "location": "Amboseli",
                "image": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1200&q=80",
                "desc": "Famous for huge elephant herds and breathtaking views of Mount Kilimanjaro.",
                "days": [
                    ("Nairobi to Amboseli", "Drive south to Amboseli. Afternoon game drive with Kilimanjaro backdrops."),
                    ("Full Day with Elephants", "Full day exploring the swamps and plains. Best chance to see big Tuskers."),
                    ("Morning Views & Return", "Early morning viewing of the mountain (weather permitting) and return to Nairobi.")
                ]
            },
            {
                "title": "6-Day Best of Kenya Classic",
                "price_usd": 1450.00,
                "duration": "6 Days / 5 Nights",
                "location": "Amboseli, Nakuru, Mara",
                "image": "https://images.unsplash.com/photo-1518709414768-a8c79b06a8dd?auto=format&fit=crop&w=1200&q=80",
                "desc": "The comprehensive Kenya experience. Visit three of the most iconic parks in one seamless trip.",
                "days": [
                    ("Nairobi to Amboseli", "Depart for Amboseli. Afternoon game drive."),
                    ("Amboseli to Lake Naivasha", "Drive to Naivasha. Boat ride on the lake to see Hippos."),
                    ("Naivasha to Lake Nakuru", "Short drive to Nakuru. Afternoon game drive for Rhinos."),
                    ("Nakuru to Masai Mara", "Scenic drive to the Mara via the Rift Valley."),
                    ("Full Day Mara", "The ultimate safari experience in the Mara."),
                    ("Return to Nairobi", "Final game drive and departure.")
                ]
            },
            {
                "title": "4-Day Luxury Fly-In Mara",
                "price_usd": 2200.00,
                "duration": "4 Days / 3 Nights",
                "location": "Masai Mara (Flight)",
                "image": "https://images.unsplash.com/photo-1629815777484-934c9c1b3338?auto=format&fit=crop&w=1200&q=80",
                "desc": "Skip the bumpy roads and fly directly into the action. Luxury tented camps and 4x4 Land Cruisers.",
                "days": [
                    ("Flight to Mara", "Take a morning flight from Wilson Airport. Land in the Mara for lunch and an afternoon drive."),
                    ("Luxury Safari", "Morning and afternoon game drives in a private 4x4 Land Cruiser."),
                    ("Bush Breakfast & Cats", "Bush breakfast experience followed by a hunt for the big cats."),
                    ("Flight to Nairobi", "Morning drive and flight back to Nairobi by noon.")
                ]
            },
            {
                "title": "3-Day Samburu Special 5",
                "price_usd": 650.00,
                "duration": "3 Days / 2 Nights",
                "location": "Samburu",
                "image": "https://images.unsplash.com/photo-1551009175-8a68da93d5f9?auto=format&fit=crop&w=1200&q=80",
                "desc": "Visit the dry north to see animals found nowhere else: Gerenuk, Grevy's Zebra, and Reticulated Giraffe.",
                "days": [
                    ("Nairobi to Samburu", "Drive north past Mt Kenya. Arrive for an evening game drive."),
                    ("The Special Five", "Full day searching for unique northern species and leopards."),
                    ("Return to Nairobi", "Morning drive and return to the capital.")
                ]
            },
            {
                "title": "5-Day Bush & Lake Family",
                "price_usd": 1100.00,
                "duration": "5 Days / 4 Nights",
                "location": "Naivasha & Mara",
                "image": "https://images.unsplash.com/photo-1551368945-801fb20d4367?auto=format&fit=crop&w=1200&q=80",
                "desc": "Designed for families. Includes walking safaris in Hell's Gate (Lion King setting) and boat rides.",
                "days": [
                    ("Nairobi to Hell's Gate", "Drive to Naivasha. Cycling or walking safari in Hell's Gate."),
                    ("Lake Naivasha Boat", "Morning boat safari. Relax at the lodge pool."),
                    ("Naivasha to Mara", "Drive to Masai Mara. Evening game drive."),
                    ("Mara for Kids", "Easy paced game drives focusing on elephants and lions."),
                    ("Return to Nairobi", "Leisurely breakfast and drive back.")
                ]
            },
            {
                "title": "10-Day Bush & Beach Honeymoon",
                "price_usd": 3500.00,
                "duration": "10 Days / 9 Nights",
                "location": "Mara & Diani",
                "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80",
                "desc": "The ultimate romance. 5 days of thrilling safari followed by 5 days of relaxation on Diani Beach.",
                "days": [
                    ("Arrival Nairobi", "Transfer to hotel. Dinner at Carnivore."),
                    ("Nairobi to Mara", "Drive to Mara. Luxury tented camp check-in."),
                    ("Mara Magic", "Full day safari with sundowners."),
                    ("Hot Air Balloon", "Sunrise balloon flight (Optional)."),
                    ("Mara to Nairobi to Diani", "Fly/Train to the Coast."),
                    ("Diani Beach", "Relaxation."),
                    ("Diani Beach", "Snorkeling or Diving."),
                    ("Diani Beach", "Sunset Dhow Cruise."),
                    ("Diani Beach", "Relaxation."),
                    ("Flight Home", "Transfer to Mombasa Airport.")
                ]
            },
            {
                "title": "5-Day Tsavo East & West",
                "price_usd": 750.00,
                "duration": "5 Days / 4 Nights",
                "location": "Tsavo",
                "image": "https://images.unsplash.com/photo-1449419266072-2d174828ce2d?auto=format&fit=crop&w=1200&q=80",
                "desc": "Explore the 'Man-Eaters' territory. Red elephants, lava flows, and the Mzima underwater springs.",
                "days": [
                    ("Nairobi to Tsavo West", "Drive to Tsavo West. Visit Shetani Lava flow."),
                    ("Mzima Springs", "Visit the underwater hippo viewing tank."),
                    ("Tsavo West to East", "Cross over to the vast Tsavo East."),
                    ("Red Elephants", "Full day finding the famous red-dust elephants."),
                    ("Return to Nairobi", "Morning drive and return.")
                ]
            },
            {
                "title": "8-Day Photographer's Paradise",
                "price_usd": 2800.00,
                "duration": "8 Days / 7 Nights",
                "location": "Amboseli, Naivasha, Mara",
                "image": "https://images.unsplash.com/photo-1470165518985-23c5d8004f2f?auto=format&fit=crop&w=1200&q=80",
                "desc": "Slower paced itinerary designed for the golden hour lighting and rare shot opportunities.",
                "days": [
                    ("Nairobi to Amboseli", "Evening shoot: Kilimanjaro sunset."),
                    ("Amboseli Full Day", "Morning shoot: Elephant herds crossing the dry lake."),
                    ("Amboseli to Naivasha", "Sunset boat ride photography."),
                    ("Crescent Island", "Walking safari for close-ups of Giraffe."),
                    ("Naivasha to Mara", "Golden hour drive."),
                    ("Mara Predators", "Focus on Lion prides."),
                    ("Mara Migration/Crossing", "Waiting for the perfect river shot."),
                    ("Return to Nairobi", "Editing time and departure.")
                ]
            }
        ]

        count = 0
        for item in safaris:
            # Check if exists to avoid duplicates
            if not SafariPackage.objects.filter(title=item["title"]).exists():
                safari = SafariPackage.objects.create(
                    title=item["title"],
                    price_usd=item["price_usd"],
                    duration_text=item["duration"],
                    location=item["location"],
                    image_url=item["image"],
                    description=item["desc"],
                    price_guideline=f"From ${item['price_usd']} pp"
                )
                
                # Add Itinerary Days
                for i, (day_title, day_desc) in enumerate(item["days"], 1):
                    ItineraryDay.objects.create(
                        safari=safari,
                        day_number=i,
                        title=day_title,
                        description=day_desc
                    )
                
                self.stdout.write(self.style.SUCCESS(f"Created: {item['title']}"))
                count += 1
            else:
                self.stdout.write(f"Skipped: {item['title']} (Already exists)")

        self.stdout.write(self.style.SUCCESS(f"Successfully added {count} new safaris!"))
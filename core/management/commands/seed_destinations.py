from django.core.management.base import BaseCommand
from django.utils.text import slugify
from core.models import Destination

class Command(BaseCommand):
    help = 'Seeds the database with 20 top Kenyan destinations'

    def handle(self, *args, **kwargs):
        destinations = [
            {
                "name": "Masai Mara",
                "subtitle": "The World Cup of Wildlife",
                "desc": "Globally famous for its exceptional population of lions, leopards, and cheetahs, and the annual migration of zebra, Thomson's gazelle, and wildebeest to and from the Serengeti every year.",
                "image": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1200&q=80",
                "best_time": "July to October (Migration)",
                "ideal_stay": "3-4 Days",
                "wildlife": "Big 5, Wildebeest, Cheetah",
                "highlights": "Great Migration, Hot Air Balloon Safaris, Mara River Crossing"
            },
            {
                "name": "Amboseli National Park",
                "subtitle": "Land of Giants",
                "desc": "Crowned by Mount Kilimanjaro, Africa's highest peak, the Amboseli National Parks is one of Kenya's most popular parks. The name 'Amboseli' comes from a Maasai word meaning 'salty dust'.",
                "image": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1200&q=80",
                "best_time": "June to October",
                "ideal_stay": "2-3 Days",
                "wildlife": "Large Elephant Herds, Lion, Buffalo",
                "highlights": "Mt Kilimanjaro Views, Observation Hill, Elephant Research"
            },
            {
                "name": "Diani Beach",
                "subtitle": "Africa's Leading Beach Destination",
                "desc": "A flawless stretch of white sand hugged by lush forest and kissed by surfable waves, Diani Beach is popular for a reason. It has been voted Africa's leading beach destination for 5 years running.",
                "image": "https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?auto=format&fit=crop&w=1200&q=80",
                "best_time": "October to March",
                "ideal_stay": "4-7 Days",
                "wildlife": "Colobus Monkeys, Dolphins, Whale Sharks",
                "highlights": "Snorkeling, Kitesurfing, Skydiving, Kongo Mosque"
            },
            {
                "name": "Tsavo East",
                "subtitle": "The Theatre of the Wild",
                "desc": "One of the oldest and largest parks in Kenya. It is famous for its large numbers of red-dusted elephants and the man-eating lions of Tsavo legend.",
                "image": "https://images.unsplash.com/photo-1449419266072-2d174828ce2d?auto=format&fit=crop&w=1200&q=80",
                "best_time": "June to October",
                "ideal_stay": "2-3 Days",
                "wildlife": "Red Elephants, Lion, Hirola",
                "highlights": "Aruba Dam, Mudanda Rock, Yatta Plateau"
            },
            {
                "name": "Lake Nakuru",
                "subtitle": "The Bird Watcher's Paradise",
                "desc": "On the floor of the Great Rift Valley, surrounded by wooded and bushy grassland, lies the beautiful Lake Nakuru. It is a UNESCO World Heritage site famous for flamingos and rhinos.",
                "image": "https://images.unsplash.com/photo-1522434526549-34301625f9b4?auto=format&fit=crop&w=1200&q=80",
                "best_time": "Year Round",
                "ideal_stay": "1-2 Days",
                "wildlife": "Rhino (Black & White), Flamingo, Leopard",
                "highlights": "Flamingo flocks, Rhino Sanctuary, Makalia Falls"
            },
            {
                "name": "Ol Pejeta Conservancy",
                "subtitle": "Home of the Last Northern White Rhinos",
                "desc": "A non-profit wildlife conservancy in Central Kenya's Laikipia County. It is the largest black rhino sanctuary in East Africa and home to two of the world's last remaining northern white rhinos.",
                "image": "https://images.unsplash.com/photo-1535591273668-578e31182c4f?auto=format&fit=crop&w=1200&q=80",
                "best_time": "June to September",
                "ideal_stay": "2-3 Days",
                "wildlife": "Rhino, Chimpanzee, Wild Dog",
                "highlights": "Chimpanzee Sanctuary, Northern White Rhinos, Night Game Drives"
            },
            {
                "name": "Samburu National Reserve",
                "subtitle": "The Special Five",
                "desc": "Located on the banks of the Ewaso Ng'iro river in Kenya. This dry, rugged paradise is home to species found nowhere else in the south, known as the Samburu Special Five.",
                "image": "https://images.unsplash.com/photo-1551009175-8a68da93d5f9?auto=format&fit=crop&w=1200&q=80",
                "best_time": "June to October",
                "ideal_stay": "3 Days",
                "wildlife": "Gerenuk, Grevy's Zebra, Beisa Oryx",
                "highlights": "Ewaso Ng'iro River, Samburu Culture, Reticulated Giraffe"
            },
            {
                "name": "Lake Naivasha",
                "subtitle": "The Rift Valley Retreat",
                "desc": "A freshwater lake in the Kenya Rift Valley. The name derives from the local Maasai name Nai'posha, meaning 'rough water'. It is a top spot for boat safaris and hippos.",
                "image": "https://images.unsplash.com/photo-1620215950835-24b89e2c6579?auto=format&fit=crop&w=1200&q=80",
                "best_time": "Year Round",
                "ideal_stay": "1-2 Days",
                "wildlife": "Hippo, Fish Eagle, Giraffe",
                "highlights": "Boat Safari, Crescent Island Walk, Flower Farms"
            },
            {
                "name": "Hell's Gate National Park",
                "subtitle": "Walk on the Wild Side",
                "desc": "Named for the intense geothermal activity within its boundaries, the Hell's Gate National Park is a remarkable quarter of the Great Rift Valley where you can cycle past zebras.",
                "image": "https://images.unsplash.com/photo-1551368945-801fb20d4367?auto=format&fit=crop&w=1200&q=80",
                "best_time": "June to March",
                "ideal_stay": "1 Day",
                "wildlife": "Zebra, Hartebeest, Baboon",
                "highlights": "Cycling Safari, Rock Climbing, Geothermal Spa"
            },
            {
                "name": "Watamu Marine Park",
                "subtitle": "Turtle Bay",
                "desc": "A small town located approximately 105 km north of Mombasa. It boasts white sand beaches and offshore coral formations arranged in different bays.",
                "image": "https://images.unsplash.com/photo-1586164273873-19cb9076040e?auto=format&fit=crop&w=1200&q=80",
                "best_time": "October to April",
                "ideal_stay": "3-5 Days",
                "wildlife": "Sea Turtles, Dolphins, Coral Fish",
                "highlights": "Gede Ruins, Bio-Ken Snake Farm, Snorkeling"
            },
            {
                "name": "Tsavo West",
                "subtitle": "Land of Lava and Springs",
                "desc": "Known for the Mzima Springs, Shetani Lava Flow, and excellent bird watching. It creates a magnificent backdrop for wildlife photography.",
                "image": "https://images.unsplash.com/photo-1626343527265-4f36c5890250?auto=format&fit=crop&w=1200&q=80",
                "best_time": "June to October",
                "ideal_stay": "2 Days",
                "wildlife": "Leopard, Rhino, Elephant",
                "highlights": "Mzima Springs, Shetani Lava Flow, Ngulia Sanctuary"
            },
            {
                "name": "Lamu Island",
                "subtitle": "Swahili Heritage",
                "desc": "Kenya's oldest living town and a UNESCO World Heritage site. Lamu is a place where donkeys are the main mode of transport and history lives in the walls.",
                "image": "https://images.unsplash.com/photo-1596395343467-f74f762744c7?auto=format&fit=crop&w=1200&q=80",
                "best_time": "December to March",
                "ideal_stay": "4-5 Days",
                "wildlife": "Donkeys, Marine Life",
                "highlights": "Lamu Old Town, Dhow Sailing, Shela Beach"
            },
            {
                "name": "Mount Kenya",
                "subtitle": "The Throne of God",
                "desc": "The second-highest mountain in Africa. It offers pristine wilderness, lakes, tarns, glaciers, and peaks of great beauty for hikers and climbers.",
                "image": "https://images.unsplash.com/photo-1627993072173-049d01249b6b?auto=format&fit=crop&w=1200&q=80",
                "best_time": "Jan-Feb, Aug-Sep",
                "ideal_stay": "4-5 Days (Climb)",
                "wildlife": "Hyrax, Duiker, Elephant (lower slopes)",
                "highlights": "Point Lenana, Hiking, Alpine Lakes"
            },
            {
                "name": "Aberdare National Park",
                "subtitle": "Majestic Moorlands",
                "desc": "A high altitude national park created to protect the slopes of the Aberdare mountain range. Known for its majestic waterfalls and dense forests.",
                "image": "https://images.unsplash.com/photo-1626507978285-8424075b2230?auto=format&fit=crop&w=1200&q=80",
                "best_time": "Year Round",
                "ideal_stay": "2 Days",
                "wildlife": "Bongo, Black Leopard, Elephant",
                "highlights": "Karuru Falls, The Ark Lodge, Trout Fishing"
            },
            {
                "name": "Meru National Park",
                "subtitle": "Born Free Country",
                "desc": "Wild and beautiful, straddling the equator and bisected by 13 rivers and numerous mountain-fed streams. This is where Elsa the lioness was released.",
                "image": "https://images.unsplash.com/photo-1456926631375-92c8ce872def?auto=format&fit=crop&w=1200&q=80",
                "best_time": "June to September",
                "ideal_stay": "3 Days",
                "wildlife": "Lion, Elephant, Rhino",
                "highlights": "Elsa's Kopje, Adamson's Falls, Wilderness"
            },
            {
                "name": "Nairobi National Park",
                "subtitle": "The World's Only Wildlife Capital",
                "desc": "The only national park that borders a capital city. You can see lions hunting with skyscrapers in the background.",
                "image": "https://images.unsplash.com/photo-1627544322695-8d5f66144e51?auto=format&fit=crop&w=1200&q=80",
                "best_time": "Year Round",
                "ideal_stay": "Half Day",
                "wildlife": "Lion, Rhino, Giraffe",
                "highlights": "Ivory Burning Site, Safari Walk, City Backdrop"
            },
            {
                "name": "Lewa Wildlife Conservancy",
                "subtitle": "Exclusive Rhino Sanctuary",
                "desc": "A UNESCO World Heritage Site and a model for community-centric conservation. It hosts the famous Lewa Marathon.",
                "image": "https://images.unsplash.com/photo-1541410965313-d53b3c16ef17?auto=format&fit=crop&w=1200&q=80",
                "best_time": "June to October",
                "ideal_stay": "3 Days",
                "wildlife": "Grevy's Zebra, Rhino (Black & White)",
                "highlights": "Horseback Safari, Rhino Conservation, Luxury Pods"
            },
            {
                "name": "Kisite Mpunguti",
                "subtitle": "Home of the Dolphins",
                "desc": "A protected marine park in the south coast of Kenya near Wasini Island. It is famous for its population of dolphins and pristine coral reefs.",
                "image": "https://images.unsplash.com/photo-1560263654-e0e64c1e451b?auto=format&fit=crop&w=1200&q=80",
                "best_time": "October to March",
                "ideal_stay": "1 Day Trip",
                "wildlife": "Dolphins, Turtles, Whales (Seasonal)",
                "highlights": "Dolphin Watching, Snorkeling, Wasini Island Lunch"
            },
            {
                "name": "Lake Bogoria",
                "subtitle": "The Geyser Lake",
                "desc": "A saline, alkaline lake that lies in a volcanic region south of Lake Baringo. It is famous for its hot springs and geysers.",
                "image": "https://images.unsplash.com/photo-1585641490226-f4460029b9f7?auto=format&fit=crop&w=1200&q=80",
                "best_time": "Year Round",
                "ideal_stay": "1-2 Days",
                "wildlife": "Flamingo, Kudu",
                "highlights": "Hot Springs, Geysers, Flamingo flocks"
            },
            {
                "name": "Chyulu Hills",
                "subtitle": "The Green Hills of Africa",
                "desc": "A mountain range in eastern Kenya which forms a volcanic field of over 100 small flows and cones. Ernest Hemingway's 'Green Hills of Africa'.",
                "image": "https://images.unsplash.com/photo-1518182170546-0766aa6f7109?auto=format&fit=crop&w=1200&q=80",
                "best_time": "June to October",
                "ideal_stay": "2-3 Days",
                "wildlife": "Elephant, Buffalo, Leopard",
                "highlights": "Leviathan Cave (Lava Tube), Cloud Forest, Views"
            }
        ]

        count = 0
        for item in destinations:
            if not Destination.objects.filter(name=item["name"]).exists():
                Destination.objects.create(
                    name=item["name"],
                    slug=slugify(item["name"]),
                    subtitle=item["subtitle"],
                    image_url=item["image"],
                    description=item["desc"],
                    best_time=item["best_time"],
                    ideal_stay=item["ideal_stay"],
                    wildlife=item["wildlife"],
                    highlights=item["highlights"]
                )
                self.stdout.write(self.style.SUCCESS(f"Created: {item['name']}"))
                count += 1
            else:
                self.stdout.write(f"Skipped: {item['name']} (Already exists)")

        self.stdout.write(self.style.SUCCESS(f"Successfully added {count} new destinations!"))
from abc import ABC, abstractmethod

# ---------------------------
# PART A — Your own class
# ---------------------------

class Device:
    """Base class (parent) with shared attributes/behaviour."""
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def info(self) -> str:
        return f"{self.brand} {self.model}"


class Smartphone(Device):
    """
    Derived class (child) showing:
      • Constructor with unique attributes
      • Encapsulation via @property (battery clamped 0–100)
      • Methods that act on state
    """
    def __init__(self, brand: str, model: str, storage_gb: int, battery: int) -> None:
        super().__init__(brand, model)
        self.storage_gb = storage_gb
        self._battery = 0
        self.battery = battery  # uses the setter to clamp

    @property
    def battery(self) -> int:
        return self._battery

    @battery.setter
    def battery(self, value: int) -> None:
        # Clamp to 0..100 to protect internal state (encapsulation)
        self._battery = max(0, min(100, int(value)))

    def call(self, number: str) -> None:
        print(f"📞 Calling {number} from {self.info()}...")

    def charge(self, amount: int) -> None:
        self.battery = self.battery + amount
        print(f"🔋 Battery now {self.battery}%")

    def use(self, minutes: int) -> None:
        # Simple drain model: 1% per 5 minutes (at least 1%)
        drain = max(1, minutes // 5)
        self.battery = self.battery - drain
        print(f"🕒 Used for {minutes} min, battery {self.battery}%")

    def __str__(self) -> str:
        return f"{self.info()} | {self.storage_gb}GB | Battery: {self.battery}%"


def demo_part_a():
    print("— PART A: Custom class with inheritance & encapsulation —")
    phone1 = Smartphone("Apple", "iPhone 14", 256, 80)
    phone2 = Smartphone("Samsung", "Galaxy S22", 128, 55)

    print(phone1)
    phone1.call("123-456-7890")
    phone1.use(30)     # drains battery
    phone1.charge(15)  # charges battery
    print(phone1)

    print(phone2)
    phone2.use(8)
    print(phone2)


# ---------------------------
# PART B — Polymorphism
# ---------------------------

class Vehicle(ABC):
    @abstractmethod
    def move(self) -> None:
        """Each subclass must implement its own move() behaviour."""
        pass

class Car(Vehicle):
    def move(self) -> None:
        print("🚗 Driving on the road!")

class Plane(Vehicle):
    def move(self) -> None:
        print("✈️ Flying in the sky!")

class Boat(Vehicle):
    def move(self) -> None:
        print("🚤 Sailing on the water!")

def demo_part_b():
    print("\n— PART B: Polymorphism demo —")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()


# ---------------------------
# Run both parts
# ---------------------------
if __name__ == "__main__":
    demo_part_a()
    demo_part_b()

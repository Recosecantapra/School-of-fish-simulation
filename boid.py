from vector import Vector


class Boid:

    def separation(self, fish, flock_fishes, tooClose=20, separation_factor=0.05):
        separation_vector = Vector(0,0)
        for other in flock_fishes:
            if other != fish:
                distance = fish.position.distance(other.position)
                if distance < tooClose and distance > 0:
                    separation_vector += (fish.position - other.position).normalize_vector() / distance
        return separation_vector * separation_factor

    def alignment(self, fish, flock_fishes, visible_distance=60, alignment_factor=0.05):
        alignment_vector = Vector(0,0)
        count = 0
        for other in flock_fishes:
            if other != fish:
                distance = fish.position.distance(other.position)
                if distance < visible_distance:
                    alignment_vector += other.velocity
                    count += 1
        if count > 0:
            alignment_vector /= count
            alignment_vector = alignment_vector - fish.velocity
            return alignment_vector.normalize_vector() * alignment_factor
        return Vector(0,0)

    def cohesion(self, fish, flock_fishes, visible_distance=60, cohesion_factor=0.005):
        cohesion_vector = Vector(0,0)
        count = 0
        for other in flock_fishes:
            if other != fish:
                distance = fish.position.distance(other.position)
                if distance < visible_distance:
                    cohesion_vector += other.position
                    count += 1
        if count > 0:
            cohesion_vector /= count
            cohesion_vector = cohesion_vector - fish.position
            return cohesion_vector.normalize_vector() * cohesion_factor
        return Vector(0,0)
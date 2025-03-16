import pygame
from components.collider import Collider
from entities.bird import Bird
from entities.ground import Ground
from entities.sky import Sky

class CollisionSystem:
    def update(self, entities):
        bird = None
        pipes = []
        ground = None
        sky = None

        for entity in entities:
            if isinstance(entity, Bird):
                bird = entity
            elif isinstance(entity, Ground):
                ground = entity
            elif isinstance(entity, Sky):
                sky = entity
            elif entity.has_component(Collider):
                pipes.append(entity)

        if bird and bird.has_component(Collider):
            bird_collider = bird.get_component(Collider)
            for pipe in pipes:
                pipe_collider = pipe.get_component(Collider)
                if bird_collider.rect.colliderect(pipe_collider.rect):
                    return True

            if ground and bird_collider.rect.colliderect(ground.collider.rect):
                return True

            if sky and bird_collider.rect.colliderect(sky.collider.rect):
                return True

        return False
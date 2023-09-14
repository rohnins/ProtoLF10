#include <SDL.h>
#include <SDL_mixer.h>

int main(int argc, char* argv[]) {
    // Initialize SDL.
    if (SDL_Init(SDL_INIT_AUDIO) < 0) {
        printf("SDL initialization failed: %s\n", SDL_GetError());
        return 1;
    }

    // Initialize SDL_mixer.
    if (Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, 2, 2048) < 0) {
        printf("SDL_mixer initialization failed: %s\n", Mix_GetError());
        return 1;
    }

    // Load an audio file.
    Mix_Chunk* sound = Mix_LoadWAV("sample.wav");
    if (sound == NULL) {
        printf("Failed to load audio: %s\n", Mix_GetError());
        return 1;
    }

    // Play the loaded audio.
    Mix_PlayChannel(-1, sound, 0);

    // Wait for audio to finish playing.
    while (Mix_Playing(-1) != 0) {
        SDL_Delay(100);
    }

    // Clean up and quit SDL.
    Mix_FreeChunk(sound);
    Mix_CloseAudio();
    SDL_Quit();

    return 0;
}

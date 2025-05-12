<template>
  <div
    v-if="visible"
    class="fixed inset-0 bg-black/60 flex items-center justify-center z-50"
  >
    <div class="bg-white rounded-lg w-full max-w-md p-6 shadow-lg">
      <h2 class="text-lg font-semibold mb-4 text-center text-red-600">
        Confirm Delete
      </h2>
      <p class="text-gray-700 mb-6 text-center">
        Are you sure you want to delete <strong>{{ itemName }}</strong
        >? This action cannot be undone.
      </p>

      <div class="flex justify-center gap-4">
        <button
          @click="close"
          class="px-4 py-2 rounded border text-gray-700 hover:bg-gray-100"
        >
          Cancel
        </button>
        <button
          @click="confirm"
          class="px-4 py-2 rounded bg-red-600 text-white hover:bg-red-700"
        >
          Delete
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  visible: Boolean,
  itemName: {
    type: String,
    default: "this item",
  },
});
const emit = defineEmits(["close", "confirm"]);

function close() {
  emit("close");
}

function confirm() {
  emit("confirm");
}
</script>
